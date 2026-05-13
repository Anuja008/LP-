Apex Application in Salesforce.com using Apex Programming Language
Main Focus
Salesforce basics
Apex programming
Custom Objects
Fields
App creation
Linear Search in Apex
Execute Anonymous Window


Step 1: Login to Salesforce
         Open browser.Go to Salesforce Login

Step 2: Open Setup
       Click Gear Icon (⚙️)
       Click Setup
Step 3: Open Object Manager
        
Step 4: Create Custom Object
        Click:Create Custom Object 

        Fill details:
    Field	Value
    1.Label	Student
   2. Plural Label	Students
    3.Object Name	Student
    4.Record Name	Student_Name
    5.Data Type	Text

    Tick:
    Allow Reports
    Allow Activities

    Click:
    Save

Step 5: Create Roll Number Field
    Inside Student Object:
    Click Fields & Relationships
    Click New

    Choose: Number
    Fill:
    Field	Value
    Field Label	Roll Number
    Length	18
    Decimal Places	0

    Click:
    Next
    Next
    Save

    Field created: Roll_Number__c
Step 6: Create Student Records
        Open: App Launcher
        Students Tab
        Click:New

        Enter:
        Student Name	Roll Number
            Anuja	1
            Rahul	2

            Click Save.

Step 7: Open Developer Console
        Click Gear Icon
        Click:Developer Console

Step 8: Create Apex Class
        In Developer Console:
            File
            New
            Apex Class
            Class Name: LinearSearchDemo
Step 9: Write Apex Code

public class LinearSearchDemo {

    public static void searchStudent(Integer rollNo) {

        List<Student__c> students =
        [SELECT Name, Roll_Number__c FROM Student__c];

        Boolean found = false;

        for(Student__c s : students) {

            if(s.Roll_Number__c == rollNo) {

                System.debug('Student Found: ' + s.Name);

                found = true;
            }
        }

        if(found == false) {

            System.debug('Student Not Found');
        }
    }
}

Click:

Save
Step 10: Execute Apex Code
        In Developer Console:
        Debug
        Open Execute Anonymous Window
        Write:

       LinearSearchDemo.searchStudent(1);

        Click: Execute

Step 11: Check Output

Open: Logs
    Debug Log

    Output:  Student Found: Anuja

    If roll number does not exist:

Student Not Found
