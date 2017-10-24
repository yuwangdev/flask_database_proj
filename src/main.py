import os
import logging

from flask import Flask, render_template, redirect, url_for, request, session

from setting import get_project_root_path

from src.data_service.Login_DataService import Login_DataService

from src.data_service.MainMenu_DataService import MainMenu_DataService

from src.data_service.Add_Incident_Dataservice import Add_Incident_DataService

from src.data_service.UserType_DataService import UserType_DataService

from src.data_service.Add_Resource_DataService import Add_Resource_DataService

from src.data_service.Search_Resource_Dataservice import Search_Resource_DataService

from src.data_service.Search_Result_Dataservice import Search_Result_DataService

from src.data_service.ResourceReport_Dataservice import ResourceReport_DataService

from src.data_service.ResourceStatus_Dataservice import ResourceStatus_DataService

from src.data_service.ActionButton_Dataservice import ActionButton_Dataservice

from datetime import datetime, timedelta

app = Flask(__name__, template_folder='../templates')

ROOT = get_project_root_path()
app.secret_key = "testtesttest"


@app.route('/')
def main():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    lds = Login_DataService()

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        check = lds.login_check_credential(str(username), str(password))

        assert isinstance(check, bool)

        if check == False:
            error = 'Invalid Credentials. Please try again.'

        else:
            session['username'] = username
            return redirect(url_for('mainMenu'))

    return render_template('login.html', error=error)


@app.route('/mainMenu')
def mainMenu():
    error = None
    mmds = MainMenu_DataService()

    username = str(session['username'])
    utDS = UserType_DataService()
    userInfo = utDS.get_title_info(username)
    print userInfo

    return render_template('mainMenu.html', name=username, userInfo=userInfo)


@app.route('/AddEmergencyIncident', methods=['GET', 'POST'])
def addIncident():
    error = None
    username = str(session['username'])
    addIncidentDS = Add_Incident_DataService(username)
    incidentID = addIncidentDS.get_new_generated_incident_id()

    if request.method == 'POST':

        if request.form['submit'] == 'Cancel':
            return redirect(url_for('mainMenu'))
        elif request.form['submit'] == 'Save':
            incidentDate = str(request.form['date'])
            incidentDes = str(request.form['description'])
            incidentLat = float(request.form['lat'])
            incidentLong = float(request.form['lng'])

            addIncidentDS.submit_form_for_new_incident(incidentDate, incidentDes, incidentLat, incidentLong)
            # print incidentDate, incidentDes, incidentLat, incidentLong
            return redirect(url_for('mainMenu'))
        else:
            pass

    else:
        return render_template('addIncident.html', incidentID=incidentID)


@app.route('/AddResource', methods=['GET', 'POST'])
def addResource():
    error = None
    username = str(session['username'])
    add_Resource_DS = Add_Resource_DataService(username)
    resourceID = add_Resource_DS.get_new_generated_resource_id()
    ESFs = add_Resource_DS.populate_esf_list()
    ESFList = []
    Units = add_Resource_DS.populate_costunit_list()
    capabilitiesList = []

    for k, val in ESFs.iteritems():
        ESFList.append('# ' + str(k) + '-' + val)

    if request.method == 'POST':
        if request.form['submit'] == 'Cancel':
            return redirect(url_for('mainMenu'))
        elif request.form['submit'] == 'Add':
            cap = str(request.form['addCap'])
            capabilitiesList = [str(s) for s in cap.split(',')]

            return render_template('addResource.html', resourceID=resourceID, owner=username, ESFs=ESFList,
                                   Units=Units, capabilities=capabilitiesList)

        elif request.form['submit'] == 'Save':
            ResourceName = str(request.form['resourceName'])
            model = str(request.form['model'])
            Latitude = float(request.form['lat'])
            Longitude = float(request.form['lng'])
            CostPerValue = float(request.form['cost'])

            CostUnit = str(request.form.get('selectedUnit'))
            customizedUnit = str(request.form['unit'])
            # if user specified customized Unit, then set the costUnit as customized unit
            if (customizedUnit):
                CostUnit = customizedUnit

            primaryESF = request.form.get('primaryESF')
            EsfID = int(primaryESF.split('-')[0].split()[1])

            additionalESF = request.form.getlist('additionalESFs')
            additionalESFList = [int(s.split('-')[0].split()[1]) for s in additionalESF]

            capabilities = request.form.getlist('capabilities')
            capabilitiesList = [str(s) for s in capabilities]
            # print capabilities
            add_Resource_DS.submit_form_for_new_resource(ResourceName, model, Latitude, Longitude,
                                                         CostPerValue, EsfID, CostUnit, additionalESFList,
                                                         capabilitiesList)
            return redirect(url_for('mainMenu'))
    return render_template('addResource.html', resourceID=resourceID, owner=username, ESFs=ESFList,
                           Units=Units, capabilities=capabilitiesList)


@app.route('/ResourceReport', methods=['GET', 'POST'])
def ResourceReport():
    error = None
    username = str(session['username'])
    resource_report_DS = ResourceReport_DataService()
    totalData = resource_report_DS.totaldata()
    usedData = resource_report_DS.usedata()

    items = []
    for i in range(0, len(totalData)):
        if (i > len(usedData) - 1):
            temp = totalData[i]
            inuseNum = 0
            temp.append(inuseNum)
            items.append(temp)
            break

        temp = totalData[i]
        inuseNum = usedData[i][2]
        temp.append(inuseNum)
        items.append(temp)

    if request.method == 'POST':
        if request.form['submit'] == 'Return':
            return redirect(url_for('mainMenu'))
        else:
            pass
    else:
        return render_template('resourceReport.html', items=items)

    return render_template('resourceReport.html', items=items)


@app.route('/ResourceStatus', methods=['GET', 'POST'])
def ResourceStatus():
    error = None
    username = str(session['username'])
    resource_status_DS = ResourceStatus_DataService()

    itemsInUse = resource_status_DS.populate_res_in_use_tabledata(username)

    print itemsInUse
    requestedByMe = resource_status_DS.res_request_by_username(username)

    receivededByMe = resource_status_DS.request_received_me(username)[0]
    # convert the previous to the list
    receivededByMeNew = []
    temp = []
    for i in receivededByMe:
        i = str(i)
        temp.append(i)
        if (len(temp) == 7):
            receivededByMeNew.append(temp)
            temp = []

    repairTable = resource_status_DS.repairtable(username)
    # print requestedByMe
    # print '-----'
    # print receivededByMe
    # print '-----'
    # print repairTable

    # return render_template('ResourceStatus.html', itemsInUse=itemsInUse,
    #                        requestedByMe=requestedByMe,
    #                        receivededByMeNew=receivededByMeNew,
    #                        repairTable=repairTable)

    if request.method == 'POST':
        if request.form['submit'] == 'BackToMainMenu':
            return redirect(url_for('mainMenu'))
        else:
            pass

    return render_template('ResourceStatus.html', itemsInUse=itemsInUse,
                           requestedByMe=requestedByMe,
                           receivededByMeNew=receivededByMeNew,
                           repairTable=repairTable)


################################################################################
# only to show how to use the form button to request for action on the webpage
# the idea should be the same with the resource search page
###############################################################################
@app.route('/buttondemo', methods=['GET'])
def button_demo():
    res_status_ds = ResourceStatus_DataService()

    resource_in_use_table_data = res_status_ds.populate_res_in_use_tabledata("james")

    assert isinstance(resource_in_use_table_data, list)

    logging.debug(resource_in_use_table_data)

    return render_template('buttondemo.html', items=resource_in_use_table_data)


################################################################################
# the method to really handle the button -Return
###############################################################################
@app.route('/ReturnButton/<resid>', methods=['GET'])
def ReturnButton(resid):
    res_status_ds = ResourceStatus_DataService()
    resource_id = int(resid)

    logging.debug("resource_id from webpage is: " + str(resource_id))
    ############################################################################################################

    res_status_ds.return_button(resource_id)
    # return str(resource_id)
    return redirect("/ResourceStatus")


################################################################################
# the method to really handle the button in the resource request by me
###############################################################################
@app.route('/ResourceRequestByMeCancelButton/<resid>/<indcidentid>', methods=['GET'])
def ResourceRequestByMeCancelButton(resid, indcidentid):
    res_status_ds = ResourceStatus_DataService()

    resource_id = int(resid)
    indicent_id = int(indcidentid)

    logging.debug("resource_id from webpage is: " + str(resource_id))
    logging.debug("incident_id from webpage is: " + str(indicent_id))
    ############################################################################################################

    res_status_ds.cancel_button(resource_id, indicent_id)

    return redirect("/ResourceStatus")


################################################################################
# the method to really handle the button Request Received By Me Reject
###############################################################################
@app.route('/RequestReceivedByMeRejectButton/<resid>/<indcidentid>', methods=['GET'])
def RequestReceivedByMeRejectButton(resid, indcidentid):
    res_status_ds = ResourceStatus_DataService()

    resource_id = int(resid)
    indicent_id = int(indcidentid)

    logging.debug("resource_id from webpage is: " + str(resource_id))
    logging.debug("incident_id from webpage is: " + str(indicent_id))

    # for debugging
    # return str(resource_id) + ': ' + str(indicent_id)

    res_status_ds.reject_button(resource_id, indicent_id)
    return redirect("/ResourceStatus")


################################################################################
# the method to really handle the button Request Received By Me Deploy
###############################################################################
@app.route('/RequestReceivedByMeDeployButton/<resid>/<erd>/<indcidentid>', methods=['GET'])
def RequestReceivedByMeDeployButton(resid, erd, indcidentid):
    res_status_ds = ResourceStatus_DataService()

    resource_id = int(resid)
    endDate = str(erd)
    username = str(session['username'])
    indicent_id = int(indcidentid)

    logging.debug("resource_id from webpage is: " + str(resource_id))
    logging.debug("incident_id from webpage is: " + str(endDate))
    logging.debug("resource_id from webpage is: " + str(username))
    logging.debug("incident_id from webpage is: " + str(indicent_id))

    # for debugging
    # return str(resource_id) + ': ' + str(indicent_id) + ': ' + username + ': ' + endDate

    res_status_ds.deploy_button(resource_id, endDate, username, indicent_id)
    return redirect("/ResourceStatus")


################################################################################
# the method to really handle the button in repairts scheduled/in-progress
###############################################################################
@app.route('/RepairCancelButton/<resid>', methods=['GET'])
def button_return_demo(resid):
    res_status_ds = ResourceStatus_DataService()

    resource_id = int(resid)

    logging.debug("resource_id from webpage is: " + str(resource_id))

    ############################################################################################################
    res_status_ds.cancelrepair_button(resource_id)

    return redirect("/ResourceStatus")


# ===================================Jianyi================================================


@app.route('/SearchResource', methods=['GET', 'POST'])
def searchResource():
    error = None
    username = str(session['username'])
    search_Resource_DS = Search_Resource_DataService(username)
    ESFs = search_Resource_DS.get_esf_lists()

    incidentList = search_Resource_DS.get_incidents_of_this_user_lists()
    # print incidentList

    if request.method == 'POST':

        if request.form['submit'] == 'Cancel':
            return redirect(url_for('mainMenu'))
        elif request.form['submit'] == 'Search':
            return redirect(url_for('searchResult'))
        else:
            pass

    else:
        return render_template('searchResource.html', ESFs=ESFs, IncidentList=incidentList)


@app.route('/searchResult', methods=['GET', 'POST'])
def searchResult():
    username = str(session['username'])
    keyword = request.form['keyword']
    ESF = request.form['ESF']
    distance = request.form['distance']
    Incident = request.form['Incident']

    logging.debug(keyword)
    logging.debug(ESF)
    logging.debug(distance)
    logging.debug("Incident is" + Incident)

    srd = Search_Result_DataService()

    if str(distance) != "":
        resp = srd.populate_table_data(str(keyword), str(ESF), int(distance), str(Incident))
    else:
        resp = srd.populate_table_data(str(keyword), str(ESF), 0, str(Incident))

    option = srd.populate_action_lists(resp, username)
    # logging.debug(option)
    assert isinstance(resp, list)

    for i in range(len(option)):
        resp[i].append(option[i])
        # logging.debug("option=" + str(option[i]))
        # logging.debug("resp=" + str(resp[i]))

    resp = sorted(resp, key=lambda x: x[0])
    resp = sorted(resp, key=lambda x: x[1])

    # get incid
    incidentID = []
    for i in range(1, len(Incident)):
        if Incident[i] == ')':
            break
        else:
            incidentID.append(Incident[i])

    incid = int("".join(incidentID))
    logging.debug(" incid = " + str(incid))

    return render_template('searchResult.html', incid=incid, resp=resp)


@app.route('/RepairFromSearch/<incid>/<resid>/', methods=['GET', 'POST'])
def RepairFromSearch(incid, resid):
    logging.debug("=======RepairFromSearch resid = " + str(resid))
    if request.method == 'POST':
        if request.form['submit'] == 'submit':
            logging.debug("=======ConfirmRepair resid = " + str(resid))

            logging.debug('success!' + incid)
            logging.debug('success!' + str(request.method))

            # get duration
            duration = request.form['duration']
            username = session['username']

            # repair request
            logging.debug(" username = " + str(username) + "; resid = " + str(resid) + '; duration=' + str(duration))
            ActionButton_DS = ActionButton_Dataservice()
            ActionButton_DS.repair_function(int(resid), str(username), int(duration))

            return 'Success!'
        else:
            return "Error: Please Check "

    return render_template('RepairFromSearch.html', incid=incid, resid=resid)


@app.route('/RequestFromSearch/<incid>/<resid>/', methods=['GET', 'POST'])
def RequestFromSearch(incid, resid):
    logging.debug("=======RequestFromSearch resid = " + str(resid))
    if request.method == 'POST':
        if request.form['submit'] == 'submit':
            logging.debug("=======ConfirmRequest resid = " + str(resid))

            logging.debug('success!: incident ID' + incid)
            logging.debug('success!: request method:' + str(request.method))

            # get expDate
            duration = request.form['duration']
            logging.debug(" duration = " + str(duration))

            duration = int(duration)
            start = datetime.now()

            end = start + timedelta(duration)

            start = datetime.strftime(start, "%Y-%m-%d")
            expDate = datetime.strftime(end, "%Y-%m-%d")
            username = session['username']
            logging.debug("======Successful until here======")

            logging.debug(" incid = " + str(incid) + "; resid = " + str(resid) + '; expDate=' + str(expDate))

            ActionButton_DS = ActionButton_Dataservice()
            ActionButton_DS.request_function(int(resid), str(expDate), int(incid))

            return 'Success!'
        else:
            return "Error: Please Check "

    return render_template('RequestFromSearch.html', incid=incid, resid=resid)


@app.route('/DeployFromSearch/<incid>/<resid>/', methods=['GET', 'POST'])
def DeployFromSearch(incid, resid):
    logging.debug("=======DeployFromSearch resid = " + str(resid))
    if request.method == 'POST':
        if request.form['submit'] == 'submit':
            logging.debug("=======ConfirmDeploy resid = " + str(resid))

            logging.debug('success!' + incid)
            logging.debug('success!' + str(request.method))

            username = session['username']
            logging.debug("======Successful until here======")

            logging.debug(" username = " + str(username) + "; resid = " + str(resid) + '; incid=' + str(incid))

            ActionButton_DS = ActionButton_Dataservice()
            ActionButton_DS.deploy_function(int(resid), int(resid), str(username))

            return 'Success!'
        else:
            return "Error: Please Check "

    return render_template('DeployFromSearch.html', incid=incid, resid=resid)


if __name__ == '__main__':
    app.run()
