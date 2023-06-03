import time 
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def getValues(serCom, input, encodeFormat):
    serCom.write(str(input).encode(encodeFormat))
    return serCom.readline().decode(encodeFormat).rstrip()

def animate(i, dataListX1, dataListY1, dataListX2, dataListY2, ser, userInput, encoding):
    dataString = getValues(ser, userInput, encoding)
    print(dataString)

    try:
        dataInt = [int(x) for x in dataString.split(',')]
        dataListX1.append(dataInt[0])
        dataListY1.append(dataInt[1])
        dataListX2.append(dataInt[3])
        dataListY2.append(dataInt[4])

    except:
        pass

    dataListX1 = dataListX1[-50:]
    dataListY1 = dataListY1[-50:]
    dataListX2 = dataListX2[-50:]
    dataListY2 = dataListY2[-50:]

    ax.clear()
    ax.plot(dataListX1)
    ax.axhline(y=500, color='red', linestyle='--', xmin=0, xmax=50)
    ax.set_ylim([0, 1024])
    ax.set_xlim([0, 50])
    ax.set_title(f"X1val = {dataInt[0]}")
    ax.set_ylabel("Value")

    ay.clear()
    ay.plot(dataListY1)
    ay.axhline(y=503, color='black', linestyle='--', xmin=0, xmax=50)
    ay.set_ylim([0, 1024])
    ay.set_xlim([0, 50])
    ay.set_title(f"Y1val = {dataInt[1]}")
    ay.set_ylabel("Value")

    ap.clear()
    ap.scatter(dataInt[0], dataInt[1])
    ap.axis('equal')
    ap.axhline(y=503, color='red', linestyle='--', xmin=0, xmax=1024)
    ap.axvline(x=500, color='black', linestyle='--', ymin=0, ymax=1024)
    ap.set_ylim([0, 1024])
    ap.set_xlim([0, 1024])
    ap.set_title("Pos data")
    ap.set_ylabel("Y1pos")
    ap.set_xlabel("X1pos")
    
    bx.clear()
    bx.plot(dataListX2)
    bx.axhline(y=500, color='red', linestyle='--', xmin=0, xmax=50)
    bx.set_ylim([0, 1024])
    bx.set_xlim([0, 50])
    bx.set_title(f"X2val = {dataInt[3]}")
    bx.set_ylabel("Value")

    by.clear()
    by.plot(dataListY2)
    by.axhline(y=503, color='black', linestyle='--', xmin=0, xmax=50)
    by.set_ylim([0, 1024])
    by.set_xlim([0, 50])
    by.set_title(f"Y2val data = {dataInt[4]}")
    by.set_ylabel("Value")

    bp.clear()
    bp.scatter(dataInt[3], dataInt[4])
    bp.axis('equal')
    bp.axhline(y=503, color='red', linestyle='--', xmin=0, xmax=1024)
    bp.axvline(x=500, color='black', linestyle='--', ymin=0, ymax=1024)
    bp.set_ylim([0, 1024])
    bp.set_xlim([0, 1024])
    bp.set_title("Pos data")
    bp.set_ylabel("Y2pos")
    bp.set_xlabel("X2pos")

    fig.tight_layout()

if __name__ == '__main__':
    ser = serial.Serial('COM7', baudrate=115200, timeout=1)

    time.sleep(3)

    dataListX1, dataListY1, dataListX2, dataListY2 = [], [], [], []

    fig = plt.figure(figsize=(12, 8)) 
    gs = fig.add_gridspec(2, 3)  
    ax = fig.add_subplot(gs[0, 0])
    ay = fig.add_subplot(gs[0, 1])
    ap = fig.add_subplot(gs[0, 2])
    bx = fig.add_subplot(gs[1, 0])
    by = fig.add_subplot(gs[1, 1])
    bp = fig.add_subplot(gs[1, 2])

    ani = animation.FuncAnimation(fig, animate, frames=100, fargs=(dataListX1, dataListY1, dataListX2, dataListY2, ser, 'y', 'ascii'), interval=10)

    plt.show()
    ser.close()