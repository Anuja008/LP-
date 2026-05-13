10.salesforce student Complaint Management System
Aim

To design and develop a custom cloud-based application using Salesforce Lightning Platform.

Step 1: Login to Salesforce
        Open browser

Step 2: Open Setup
      Click Gear Icon (⚙️)
     Click: Setup

Step 3: Open Object Manager
        In Setup Search Box type:
        Object Manager
Step 4: Create Student Object
        Click: Create Custom Object
        Fill:
    Field	Value
    Label	Student
    Plural Label	Students
    Object Name	Student
    Record Name	Student_Name

    Tick:
    Allow Reports
    Allow Activities
    Click Save.

Step 5: Create Student Fields

        Roll Number Field
        Create field:
`       Property	Value
        Data Type	Number
        Label	Roll Number

    Field API Name: Roll_Number__c

Step 6: Create Complaint Object
        Again: Object Manager
                Create
                Custom Object

        Fill:
            Field	Value
            Label	Complaint
            Plural Label	Complaints
            Object Name	Complaint
            Record Name	Complaint_Name
            Click Save.

Step 7: Create Complaint Fields
        
        Fields & Relationships
        Create fields: Field	         Type
            (field1) ComplaintText	Text Area
             {field2)Complaint Date	Date
             (field3) Status	        Picklist
                      In Values box enter:  Open
                                            Closed
                                            Pending
             (field4) Student	        Lookup(Student)

Step 8: Create Lightning App
    Go to: App Manager
    Click: New Lightning App

Step 9: Configure App
        App Name: Student Complaint System

        Click: Next
                Next

Step 10: Add Navigation Items
            Add:
                Students
                Complaints
                Reports
                Dashboards
        In User Profiles
           Add System Administrator

            Click: Save & Finish

Step 11: Open App
    Click App Launcher (9 dots)
    Search: Student Complaint System
            Open App

Step 12: Create Custom Object
        Search: Object Manager
                Create Custom Object

Step 4: Fill Object Details


 Add Student Record
        Open: Students Tab
        Click: New

    Enter:
    Student Name	Roll Number
            Anuja	1

    Click Save.

Step 13: Add Complaint Record
        Open: Complaints Tab
        Click New.
        
        Enter:

        Field	Value
    Complaint Name	Lab Issue
    Complaint Text	Computer not working
    Date	Current Date
    Status	Open
    Student	Anuja

    Click Save.

Step 14: Create Report
        Open: Reports
        Click: New Report

        Select ; Complaints
        Add fields:
                  Complaint Name
                  Student
                  Status
                  Date

        Click: Save & Run

Step 15: Create Dashboard
        Open: Dashboards
        Click: New Dashboard

   Add chart using complaint report.
   Click Save.


end--------------



Field	Use
Complaint Text	Stores complaint details
Complaint Date	Stores complaint date
Status	Shows complaint status
Student	Links complaint to student
Output

The application manages:

Student details
Complaint records
Reports
Dashboards

using Salesforce Cloud.

Concepts Used
Concept	Use
Salesforce Cloud	Application Platform
CRM	Data Management
Lightning App	UI Development
Reports	Data Analysis
Dashboard	Visualization
Advantages
Cloud-based application
Easy complaint management
Secure data storage
Fast access
Real-time reporting
Applications
College Complaint System
Employee Complaint System
Help Desk Management
Customer Support System
