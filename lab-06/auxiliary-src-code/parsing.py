import datetime
SerNo = 0

SerNo += 1
Port = "PortAlexandeia"

# Get Barcode info
print("Barcode info?")
BarcodeInfo = input()
Dest = ["Cairo", "Luxor", "Mansura"][int(BarcodeInfo[0]) - 1]
#print(Dest)
type = ["Vegetables", "Wheat", "Rice"][int(BarcodeInfo[1]) - 1]
#print(type)
weight = ["5", "10", "20"][int(BarcodeInfo[2]) - 1]
#print(weight)

current_time = datetime.datetime.now()
Year = current_time.year
Month = current_time.month
Day = current_time.day
# Day could flip in case > 24 
Hour = current_time.hour #+ 2
Minute = current_time.minute

Message = str(SerNo) + ","
Message += Port + ","
Message += str(Year) + ","
Message += str(Month) + ","
Message += str(Day) + ","
Message += str(Hour) + ","
Message += str(Minute) + ","
Message += Dest + ","
Message += type + ","
Message += weight
print(Message)
