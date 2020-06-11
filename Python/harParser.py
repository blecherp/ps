#!/usr/bin/env python3

import json
import os.path
import os
import shutil
import sys
import json


# script_dir = os.path.dirname(__file__)
logFiles_dir = sys.argv[1]
# resultFiles_dir = os.path.join(logFiles_dir, 'ParserResult/')
jsonFiles_dir = os.path.join(logFiles_dir, 'JsonFiles/')


harExtension = '.har'


# Create needed directories
# These directories get chosen by the user in the final product
# if not os.path.isdir(logFiles_dir):
#     os.makedirs(logFiles_dir)

# Remove results dir it it already exists
# Prevents exception while testing to parse the same files over and over again
# if os.path.isdir(resultFiles_dir):
#     shutil.rmtree(resultFiles_dir)
# os.makedirs(resultFiles_dir)

# Removes tmp jsonFiles_dir if it already exists
# Prevents exception if last run failed and could not remove it successfully
if os.path.isdir(jsonFiles_dir):
    shutil.rmtree(jsonFiles_dir)
os.makedirs(jsonFiles_dir)


# Change extension of tmp har file to .json
def convertToJson(filepath):
    pre, ext = os.path.splitext(filepath)
    os.rename(filepath, pre + '.json')


def webSocketParser1(index, jsonFile):

    # Store all found sessionId's and assign their index in the outputList
    # Example: All information about the host gets saved in outputList[0]. All information about player2 (networkId = p2) gets saved in outputList[1].
    ownerDict = {}
    ownerDictIndex = 0

    # Store all collected information
    outputList = []

    # Go through all objects in webSocketMessages1
    for item in jsonFile['log']['entries'][index]['_webSocketMessages']:

        sessionId = None

        dataLevel1 = json.loads(item['data'])

        time = item['time']



        if "nafr" in dataLevel1:
            lastItem = dataLevel1 [-1]

            nafString = lastItem['naf']
            nafDict = json.loads(nafString)

            dataLevel2 = nafDict['data']

            if "d" in dataLevel2.keys():
                dList = dataLevel2['d']
                dDict = dList[0]

                if dDict['template'] == "#remote-avatar":
                    sessionId = dDict['owner']
                    #networkId = dDict['networkId']

                    # Check if networkId is already known and update the ownerDict if not
                    if not sessionId in ownerDict.keys():
                        ownerDict.update({sessionId: ownerDictIndex})
                        ownerDictIndex += 1
                        outputList.append([])

                    components = dDict['components']

                    # To test the different hierarchy levels simply remove the hashtag from the following line and enter one of the variables between dataLevel1 and components
                    #print(item, "\n")

                    dataGetsStored = False
                    dataElementDict = {'time': time, 'components': []}


                    # Player Position
                    if "0" in components:
                        playerCoordinates = components['0']
                        x = playerCoordinates['x']
                        y = playerCoordinates['y']
                        z = playerCoordinates['z']

                        dataGetsStored = True

                        playerPositionDict = {'componentName': "PlayerPosition", "x" : x, "y" : y, "z" : z}
                        dataElementDict['components'].append(playerPositionDict)


                    # Player Roation
                    if "1" in components:
                        playerRotation = components['1']
                        x = playerRotation['x']
                        y = playerRotation['y']
                        z = playerRotation['z']

                        dataGetsStored = True

                        playerRotationDict = {'componentName': "PlayerRotation", "x": x, "y": y, "z": z}
                        dataElementDict['components'].append(playerRotationDict)

                    # Player Scale
                    if "2" in components:
                        playerScale = components['2']
                        x = playerScale['x']
                        y = playerScale['y']
                        z = playerScale['z']

                        dataGetsStored = True

                        playerScaleDict = {'componentName': "PlayerScale", "x": x, "y": y, "z": z}
                        dataElementDict['components'].append(playerScaleDict)



                    # Camera Position
                    if "5" in components:
                        cameraPosition = components['5']
                        x = cameraPosition['x']
                        y = cameraPosition['y']
                        z = cameraPosition['z']

                        dataGetsStored = True

                        CameraPositionDict = {'componentName': "CameraPosition", "x": x, "y": y, "z": z}
                        dataElementDict['components'].append(CameraPositionDict)



                    # Camera Rotation
                    if "6" in components:
                        cameraRotation = components['6']
                        x = cameraRotation['x']
                        y = cameraRotation['y']
                        z = cameraRotation['z']

                        dataGetsStored = True

                        CameraRotationDict = {'componentName': "CameraRotation", "x": x, "y": y, "z": z}
                        dataElementDict['components'].append(CameraRotationDict)


                    # Left Controller Position
                    if "7" in components:
                        leftControllerPosition = components['7']
                        x = leftControllerPosition['x']
                        y = leftControllerPosition['y']
                        z = leftControllerPosition['z']

                        dataGetsStored = True

                        LeftControllerPositionDict = {'componentName': "LeftControllerPosition", "x": x, "y": y, "z": z}
                        dataElementDict['components'].append(LeftControllerPositionDict)


                    # Left Controller Rotation
                    if "8" in components:
                        leftControllerRotation = components['8']
                        x = leftControllerRotation['x']
                        y = leftControllerRotation['y']
                        z = leftControllerRotation['z']

                        dataGetsStored = True

                        LeftControllerRotationDict = {'componentName': "LeftControllerRotation", "x": x, "y": y, "z": z}
                        dataElementDict['components'].append(LeftControllerRotationDict)


                    # Left Controller Visibility
                    if "9" in components:
                        LeftControllerVisibility = components['9']

                        dataGetsStored = True

                        LeftControllerVisibilityDict = {'componentName': "LeftControllerVisibility", "visible?": LeftControllerVisibility}
                        dataElementDict['components'].append(LeftControllerVisibilityDict)


                    # Right Controller Position
                    if "10" in components:
                        rightControllerPosition = components['10']
                        x = rightControllerPosition['x']
                        y = rightControllerPosition['y']
                        z = rightControllerPosition['z']

                        dataGetsStored = True

                        RightControllerPositionDict = {'componentName': "RightControllerPosition", "x": x, "y": y, "z": z}
                        dataElementDict['components'].append(RightControllerPositionDict)


                    # Right Controller Rotation
                    if "11" in components:
                        rightControllerRotation = components['11']
                        x = rightControllerRotation['x']
                        y = rightControllerRotation['y']
                        z = rightControllerRotation['z']

                        dataGetsStored = True

                        RightControllerRotationDict = {'componentName': "RightControllerRotation", "x": x, "y": y, "z": z}
                        dataElementDict['components'].append(RightControllerRotationDict)


                    # Left Controller Visibility
                    if "12" in components:
                        RightControllerVisibility = components['12']

                        dataGetsStored = True

                        RightControllerVisibilityDict = {'componentName': "RightControllerVisibility", "visible?": RightControllerVisibility}
                        dataElementDict['components'].append(RightControllerVisibilityDict)


                    if dataGetsStored:
                        outputList[ownerDict[sessionId]].append(dataElementDict)


    webSocketMessages1 = []
    for owner in ownerDict.keys():
        webSocketMessages1.append({"sessionId": owner, "data": outputList[ownerDict[owner]]})

    return webSocketMessages1


def webSocketParserInteractivePen(index, jsonFile):

    # Store all found networkId's and assign their index in the outputList
    # Example: All information about the host gets saved in outputList[0]. All information about player2 (networkId = p2) gets saved in outputList[1].
    ownerDict = {}
    ownerDictIndex = 0

    outputList = []

    drawingNameList = []


    for item in jsonFile['log']['entries'][index]['_webSocketMessages']:
        dataLevel1 = json.loads(item['data'])


        sessionId = None

        # Outgoing traffic
        if item['type'] == "send":
            lastItem = dataLevel1[-1]
            if lastItem is not None:

                if 'naf' in lastItem.keys():
                    nafString = lastItem['naf']
                    nafDict = json.loads(nafString)

                    # Name of the drawing
                    dataType = nafDict['dataType']

                    # Check if dataType really links to a drawing
                    # by checking if its value looks like "drawing-RandomChars"
                    if dataType[:7] == 'drawing':
                        dataLevel2 = nafDict['data']
                        if 'buffer' in dataLevel2.keys():
                            sessionId = 'host'

                            if not sessionId in ownerDict.keys():
                                ownerDict.update({sessionId: ownerDictIndex})
                                outputList.append([])
                                ownerDictIndex += 1

                            # Get the buffer data
                            buffer = dataLevel2['buffer']

                            bufferNr = buffer[0]
                            bX = buffer[1]
                            bY = buffer[2]
                            bZ = buffer[3]
                            time = item['time']

                            outputList[ownerDict[sessionId]].append({"bufferNr": bufferNr, "time": time, "x": bX, "y": bY, "z": bZ})

        # Incoming traffic
        if item['type'] == "receive":
            lastItem = dataLevel1[-1]
            if lastItem is not None:
                if 'naf' in lastItem.keys():
                    nafString = lastItem['naf']
                    nafDict = json.loads(nafString)

                    # Name of the drawing
                    dataType = nafDict['dataType']

                    # Check if dataType really links to a drawing
                    # by checking if its value looks like "drawing-RandomChars"
                    if dataType[:7] == 'drawing':
                        dataLevel2 = nafDict['data']

                        if 'buffer' in dataLevel2.keys():

                            sessionId = lastItem['from_session_id']

                            if not sessionId in ownerDict.keys():
                                ownerDict.update({sessionId: ownerDictIndex})
                                outputList.append([])
                                ownerDictIndex += 1

                            # Get the buffer data
                            buffer = dataLevel2['buffer']

                            bufferNr = buffer[0]
                            bX = buffer[1]
                            bY = buffer[2]
                            bZ = buffer[3]
                            time = item['time']

                            outputList[ownerDict[sessionId]].append({"bufferNr": bufferNr, "time": time, "x": bX, "y": bY, "z": bZ})

    # Store rearranged data
    correctedOutputList = []
    # Set this value to determine how many seconds need to be between two data points
    # to be seen as two distinct drawings
    secs = 4

    # Rearrange data to match the interactive_pen template
    for collection in outputList:
        correctedOutputList.append([])
        index = 0
        tmpDrawing = []
        for buffer in collection:
            if index == 0:
                tmpDrawing.append(buffer)
                index += 1
            elif index == len(collection)-1:
                tmpDrawing.append(buffer)
                correctedOutputList[-1].append(tmpDrawing)
            else:
                if (buffer['time'] - tmpDrawing[-1]['time'] > secs) & (buffer['bufferNr'] < tmpDrawing[-1]['bufferNr']) :
                    correctedOutputList[-1].append(tmpDrawing)
                    tmpDrawing = []
                    tmpDrawing.append(buffer)
                    index += 1
                else:
                    tmpDrawing.append(buffer)
                    index += 1


    # Return value
    interactive_pen = []

    # Add data to return value
    for owner in ownerDict.keys():
        template = {"sessionId": owner, "drawings": []}
        for data in correctedOutputList[ownerDict[owner]]:
            template["drawings"].append({"drawingData": data})
        interactive_pen.append(template)


    return interactive_pen


def nameMapping(index, jsonFile):
    # Go through all objects in webSocketMessages1

    sessionIDDict = {}

    for item in jsonFile['log']['entries'][index]['_webSocketMessages']:

        # Outgoing traffic
        if item['type'] == "receive":
            dataLevel1 = json.loads(item['data'])

            if "presence_diff" in dataLevel1:
                lastItem = dataLevel1[-1]

                joinString = lastItem['joins']
                if not len(joinString) == 0:
                    for key in joinString.keys():
                        sessionID = key

                        dataLevel2 = joinString[sessionID]
                        metasList = dataLevel2['metas']
                        metasDict = metasList[0]

                        #permissions of a player
                        permissionsDict = metasDict['permissions']
                        closeHubDict = permissionsDict['close_hub']
                        embedHubDict = permissionsDict['embed_hub']
                        flyDict = permissionsDict['fly']
                        joinHubDict = permissionsDict['join_hub']
                        kickUsersDict = permissionsDict['kick_users']
                        muteUsersDict = permissionsDict['mute_users']
                        pinObjectsDict = permissionsDict['pin_objects']
                        spawnAndMoveMediaDict = permissionsDict['spawn_and_move_media']
                        spawnCameraDict = permissionsDict['spawn_camera']
                        spawnDrawingDict = permissionsDict['spawn_drawing']
                        spawnEmojiDict = permissionsDict['spawn_emoji']
                        updateHubDict = permissionsDict['update_hub']
                        updateHubPromotionDict = permissionsDict['update_hub_promotion']
                        updateRolesDict = permissionsDict['update_roles']
                        allPermissionsDict = {'close_hub': closeHubDict, 'embed_hub': embedHubDict, 'fly': flyDict, 'join_hub': joinHubDict, 'kick_users': kickUsersDict, 'mute_users': muteUsersDict, 'pin_objects': pinObjectsDict, 'spawn_and_move_media': spawnAndMoveMediaDict, 'spawn_camera': spawnCameraDict, 'spawn_drawing': spawnDrawingDict, 'spawn_emoji': spawnEmojiDict, 'update_hub': updateHubDict, 'update_hub_promotion': updateHubPromotionDict, 'update_roles': updateRolesDict}


                        #roles of a player
                        rolesDict = metasDict['roles']
                        creatorDict = rolesDict['creator']
                        ownerDict = rolesDict['owner']
                        signedInDict = rolesDict['signed_in']
                        allRolesDict = {'creator': creatorDict, 'owner': ownerDict, 'signed_in': signedInDict}


                        profileDict = metasDict['profile']
                        displayName = profileDict['displayName']

                    # Check if sessionID is already known and update the sessionIDDict if not
                        if not sessionID in sessionIDDict.keys():
                            sessionIDDict.update({sessionID: {'displayName': displayName, 'permissions': allPermissionsDict, 'roles': allRolesDict}})
                            print(sessionIDDict)


            if "presence_state" in dataLevel1:
                lastItem = dataLevel1[-1]

                for key in lastItem.keys():
                    sessionID = key

                    dataLevel2 = lastItem[sessionID]
                    metasList = dataLevel2['metas']
                    metasDict = metasList[0]


                    #permissions of a player
                    permissionsDict = metasDict['permissions']
                    closeHubDict = permissionsDict['close_hub']
                    embedHubDict = permissionsDict['embed_hub']
                    flyDict = permissionsDict['fly']
                    joinHubDict = permissionsDict['join_hub']
                    kickUsersDict = permissionsDict['kick_users']
                    muteUsersDict = permissionsDict['mute_users']
                    pinObjectsDict = permissionsDict['pin_objects']
                    spawnAndMoveMediaDict = permissionsDict['spawn_and_move_media']
                    spawnCameraDict = permissionsDict['spawn_camera']
                    spawnDrawingDict = permissionsDict['spawn_drawing']
                    spawnEmojiDict = permissionsDict['spawn_emoji']
                    updateHubDict = permissionsDict['update_hub']
                    updateHubPromotionDict = permissionsDict['update_hub_promotion']
                    updateRolesDict = permissionsDict['update_roles']
                    allPermissionsDict = {'close_hub': closeHubDict, 'embed_hub': embedHubDict, 'fly': flyDict, 'join_hub': joinHubDict, 'kick_users': kickUsersDict, 'mute_users': muteUsersDict, 'pin_objects': pinObjectsDict, 'spawn_and_move_media': spawnAndMoveMediaDict, 'spawn_camera': spawnCameraDict, 'spawn_drawing': spawnDrawingDict, 'spawn_emoji': spawnEmojiDict, 'update_hub': updateHubDict, 'update_hub_promotion': updateHubPromotionDict, 'update_roles': updateRolesDict}



                    #roles of a player
                    rolesDict = metasDict['roles']
                    creatorDict = rolesDict['creator']
                    ownerDict = rolesDict['owner']
                    signedInDict = rolesDict['signed_in']
                    allRolesDict = {'creator': creatorDict, 'owner': ownerDict, 'signed_in': signedInDict}



                    profileDict = metasDict['profile']
                    displayName = profileDict['displayName']

                    if not sessionID in sessionIDDict.keys():
                        sessionIDDict.update({sessionID: {'displayName': displayName, 'permissions': allPermissionsDict, 'roles': allRolesDict}})



def messageProtocol(index, jsonFile):


    outputList = []

    # Go through all objects in webSocketMessages1
    for item in jsonFile['log']['entries'][index]['_webSocketMessages']:

        time = item['time']
        sessionId = None
        body = None

        dataLevel1 = json.loads(item['data'])

        if "message" in dataLevel1:
            lastItem = dataLevel1[-1]

            if 'session_id' in lastItem.keys():
                sessionId = lastItem['session_id']
                body = lastItem['body']

        if sessionId is not None:
            outputList.append({'sessionId': sessionId, 'time':time, 'message': body})

    return outputList



# Parses all json Files and returns found data
def jsonParser():

    # Go through every file in the LogFiles directory
    for filename in os.listdir(jsonFiles_dir):

        # Load json File
        print(filename,":\n")
        inputFile = open(os.path.join(jsonFiles_dir, filename))
        jsonFile = json.load(inputFile)
        inputFile.close()




        # Find _webSocketMessages object indices
        webSocketMessagesIndexList = []
        for index in range(len(jsonFile['log']['entries'])):
            if '_webSocketMessages' in jsonFile['log']['entries'][index].keys():
                if len(jsonFile['log']['entries'][index]['_webSocketMessages']) > 0:
                    webSocketMessagesIndexList.append(index)

        # Json Output
        fn, ext = os.path.splitext(filename)
        # fullFileName = fn + "Result.json"
        fullFileName = "Result.json"
        completePath = os.path.join(logFiles_dir, fullFileName)
        data = {}


        data.update({"#remote_avatar": webSocketParser1(webSocketMessagesIndexList[0], jsonFile)})
        data.update({"additional_templates": {"#interactive_pen": webSocketParserInteractivePen(webSocketMessagesIndexList[0], jsonFile)}})
        data.update({"chatMessages": messageProtocol(webSocketMessagesIndexList[0], jsonFile)})

        with open(completePath, "w") as write_file:
            json.dump(data, write_file, indent=4)


        # TEST Function
        nameMapping(webSocketMessagesIndexList[0], jsonFile)





# Convert all files in the LogFile directory to json and save them in the tmp directory '../JsonFiles/'
def convertHarFilesToJson():
    for filename in os.listdir(logFiles_dir):
        pre, ext = os.path.splitext(filename)

        if ext == '.har':
            srcFile = os.path.join(logFiles_dir, filename)
            shutil.copy(srcFile, jsonFiles_dir)

            convertFilePath = os.path.join(jsonFiles_dir, filename)
            convertToJson(convertFilePath)





if __name__ == "__main__":
    convertHarFilesToJson()
    jsonParser()

    shutil.rmtree(jsonFiles_dir)
    os.remove(os.path.join(logFiles_dir, "tmpHarFile.har"))

    print("Python Con Worked")

    # If you want to run HarParser in a command line window,
    # remove the hashtag from the following line to wait for user input before closing the window.
    #close = input("Press return to exit")
