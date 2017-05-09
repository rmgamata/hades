from Tkinter import *
import tkFileDialog
from decimal import *

#holly open
def extractScript():
	textfile = raw_input("> ")
	holly = open(textfile, 'r')
	x = 1
	for line in holly:
		if ".wav" in line:
			wav = line.replace('EXPECT fetch uri=.*/','').replace('.wav', '').strip()
			callflow.insert(x, wav)
			x+=1
			
#end

def steps():
	print "s"
	raw_input("")

	
def moveup():
	index = list_prompt.curselection()[0]
	seltext = list_prompt.get(index)
	pos = index - 1
	list_prompt.delete(index)
	list_prompt.insert(pos,seltext)
	
def delete():
	index = list_prompt.curselection()[0]
	seltext = list_prompt.get(index)
	list_prompt.delete(index)

def movedown():
	index = list_prompt.curselection()[0]
	seltext = list_prompt.get(index)
	pos = index + 1
	list_prompt.delete(index)
	list_prompt.insert(pos,seltext)		
	
def run():
	
	myflow = []
	countflow = callflow.size()
	f = 0
	while f < countflow:
		flow_values = callflow.get(f)
		f+=1
		myflow.append(flow_values)
	print myflow
	c = 0
	match = 0
	while c < countflow:
		step_values = list_prompt.get(c)
		if step_values in myflow:
			step_index = list_prompt.get(0, END).index(step_values) #get index of prompt that match
			match +=1
			if match == 1:
				break
	
			c+=1

	countsteps = list_prompt.size()
	print "total number of steps: ", countsteps
	flow_index = callflow.get(0, END).index(step_values)
	flow_values = callflow.get(flow_index)
	r = 0
	passed = 0
	failed = 0
	while r < countsteps:
		flow_values = callflow.get(flow_index)
		step_values = list_prompt.get(step_index)

		
		if step_values == flow_values:
			print "Flow: ", flow_values, "  |   Step: ", step_values
			print "PASSED"
			passed +=1
		else:
			print "Flow: ", flow_values, "  |   Step: ", step_values
			print "FAILED"
			failed = 1
		# if failed == 1:
			# break
		r+=1
		flow_index+=1
		step_index+=1
		
		
	print "Passed: ", passed
	print "TOTAL: ", countsteps
	getcontext().prec = 2
	passed = Decimal(passed)
	countsteps = Decimal(countsteps)
	percentage = Decimal(passed/countsteps)
	print percentage
	print "{:.1%}".format(percentage)

		
		
root = Tk()	
callflow = Listbox(root, height=30)
callflow.pack()


list_prompt = Listbox(root,height=30)
list_prompt.pack()
list_prompt.insert(1, "GreetingDefault")
list_prompt.insert(2, "Greeting")
list_prompt.insert(3, "ProviderOption")
list_prompt.insert(4, "GMVHits_04_Elemental")
list_prompt.insert(5, "MainMenu")
list_prompt.insert(6, "Privacy")
list_prompt.insert(7, "AskDOB")
list_prompt.insert(8, "AskDOBConf")
list_prompt.insert(9, "AskDOBConfNI1_1")
list_prompt.insert(10, "AskDOBConfNI1_2")
list_prompt.insert(11, "GetZip")
list_prompt.insert(12, "HelloName")
list_prompt.insert(13, "AppointmentDate_1")
list_prompt.insert(14, "AppointmentDate_2")
list_prompt.insert(15, "NeworExisting")
list_prompt.insert(16, "Transfer")


#RUN
run = Button(root, text="RUN", command=run)
run.pack()


#up-down-delete
moveup = Button(root, text="up", command=moveup)
moveup.pack()
delete = Button(root, text="del", command=delete)
delete.pack()
movedown = Button(root, text="down", command=movedown)
movedown.pack()
#end
	

	
if __name__ == "__main__":
	extractScript()
	steps()
	moveup()
	movedown()
	delete()