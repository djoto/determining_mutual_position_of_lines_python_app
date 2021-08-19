from math import *
from sympy import *
from sympy.plotting import plot, plot_parametric

def invalidInputMessage(dictInputs, inputType):
    
    inputsCopy = dictInputs
    
    warningMessage = ''
    
    errInputs = []
    for i in dictInputs:
        try:
            float(dictInputs[i])
            dictInputs[i] = float(dictInputs[i])
        except:
            errInputs.append(i)
            
    if errInputs != []:
        dictInputs = inputsCopy
        warningMessage = "Neispravan unos za:\n"
        for i in errInputs:
            warningMessage = warningMessage + i + ' '
        
        return warningMessage

    if inputType == 'coordinates':
    
        if samePoints(dictInputs['x11'], dictInputs['y11'], dictInputs['x12'], dictInputs['y12']):
            warningMessage = 'Neispravan unos za pravu 1:\nZa iscrtavanje prave potrebno je unijeti 2 različite tačke!'
            return warningMessage
            
        if samePoints(dictInputs['x21'], dictInputs['y21'], dictInputs['x22'], dictInputs['y22']):
            warningMessage = 'Neispravan unos za pravu 2:\nZa iscrtavanje prave potrebno je unijeti 2 različite tačke!'
            return warningMessage

    elif inputType == 'slope_intercept':

        if (dictInputs['ugao1'] < 0 or dictInputs['ugao1'] > 360):
            warningMessage = 'Neispravan unos za ugao1!\nVrijednost ugla mora biti izmedju 0° i 360°'
            return warningMessage

        if (dictInputs['ugao2'] < 0 or dictInputs['ugao2'] > 360):
            warningMessage = 'Neispravan unos za ugao2!\nVrijednost ugla mora biti izmedju 0° i 360°'
            return warningMessage
        
    return warningMessage
    

def samePoints(x1, y1, x2, y2):

    if (x1 == x2) and (y1 == y2):
        return 1

    return 0
    

def setLinFuncFromPoints(x1, y1, x2, y2):
    
    if (x2 - x1) == 0:
        Xindex = 1
        Yindex = 0
        freeIndex = -x1
    else:
        Xindex = ((y2 - y1)/(x2 - x1))
        Yindex = -1
        freeIndex = (- ((y2 - y1)/(x2 - x1)) * x1 + y1)

    return (Xindex, Yindex, freeIndex)


def setLinFuncFromSlopeIntercept(angle, intercept):
    
    if angle == 90 or angle == 270:
        Xindex = 1
        Yindex = 0
        freeIndex = -intercept
    else:
        Xindex = tan(radians(angle))
        Yindex = -1
        freeIndex = intercept
        
    return (Xindex, Yindex, freeIndex)


def stringGeneralForm(line):
    
    return '{:.2f}'.format(line[0])+'*x + '+'({:.2f})'.format(line[1])+' *y + '+'({:.2f})'.format(line[2])+' = 0\n'
    

def plotLine(line, data, intersectXabs, intersectYabs):
    
    x = symbols('x')
    y = symbols('y')
    
    if line[1] == -1:
        p = plot_parametric((x, line[0]*x + line[2], (x, -intersectXabs-10, intersectXabs+10)), show = False, xlabel="x", ylabel="y", title=data)
    else:
        p = plot_parametric((-line[2], x, (x, -intersectYabs-10, intersectYabs+10)), show = False, xlabel="x", ylabel="y", title=data)
        
    return p


def drawPlot(line1, line2):
    
    x = symbols('x')
    y = symbols('y')
    
    systemLinEqResult = solve([line1[0]*x + line1[1]*y + line1[2], line2[0]*x + line2[1]*y + line2[2]], (x, y))
    
    strFromResult = 'Opšti oblik jednačina pravih:\n'+stringGeneralForm(line1) + stringGeneralForm(line2)
    
    intersectX = 0
    intersectY = 0
    if len(systemLinEqResult) == 2:
        strFromResult += 'Prave se sijeku u tački sa koordinatama x='+'{:.2f}'.format(systemLinEqResult[x])+', y='+'{:.2f}'.format(systemLinEqResult[y])+'\n'
        intersectX = float(systemLinEqResult[x])
        intersectY = float(systemLinEqResult[y])
    elif len(systemLinEqResult) == 1:
        strFromResult += 'Prave se poklapaju.\n'
    else:
        strFromResult += 'Prave su paralelne.\n'
    
    p1 = plotLine(line1, strFromResult, abs(intersectX), abs(intersectY))
    
    p2 = plotLine(line2, strFromResult, abs(intersectX), abs(intersectY))

    p1.extend(p2)
    p1.show()
    
    return 1
