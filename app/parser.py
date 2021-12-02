def readParser(xmlTree):
  result = {}
  root = xmlTree.getroot()

  for child in root:
    time = child.get('time')
    for veh in child:
      vehid = veh.get('id')
      veh_xpos = veh.get('x')
      veh_ypos = veh.get('y')

      if vehid in result:
        result[vehid].append([time, veh_xpos, veh_ypos])
      else:
        result[vehid] = [[time, veh_xpos, veh_ypos]]

  return result

def start_end_only(original):
  
  for key in original:
    length = len(original[key])
    newlst = original[key][0]+original[key][length//3]+original[key][2*length//3]+original[key][-1]
    original[key] = newlst
    
  return original