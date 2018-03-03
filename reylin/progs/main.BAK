ON ERROR DO ErrorHandler WITH ERROR( ), MESSAGE( ), MESSAGE(1), PROGRAM( ), LINENO(1)

*!* Set up the initial environment
DO SetCommands
DO SetupScreen
DO SetupMenu
DO SetupDatabase

*!* Bring up the application form
DO FORM splash

*!* Setup Quit Routine
ON SHUTDOWN CLEAR EVENTS && if user quits app then run ProperShutdown procedure

*!* Start event processing loop
READ EVENTS

DO ProperShutdown

********************
PROCEDURE ErrorHandler
********************

   PARAMETERS tnError, tcMessage, tcMessage1, tcProgram, tnLineno
   LOCAL lcErrorMessage
   lcErrorMessage = "Error number: " + TRANSFORM(tnError) + CHR(13) ;
      + "Error message: " + tcMessage + CHR(13) ;
      + "Line of code: " + tcMessage1 + CHR(13);
      + "Program: " + tcProgram + CHR(13);
      + "Line number: " + TRANSFORM(tnLineno)
   MESSAGEBOX(lcErrorMessage, 16, "A Problem Has Been Encountered")
   CLEAR EVENTS
ENDPROC

********************
PROCEDURE SetCommands
********************
   LOCAL lcPath
   SET BELL ON && Turns the computer bell on
   SET CENTURY ON && Specifies a four-digit year in a format that includes 10 characters
   SET CONSOLE OFF && Disables output to the main Visual FoxPro window or to the active user-defined window from within programs
   SET DELETED ON && Specifies that commands that operate on records, including records in related tables, using a scope ignore records that are marked for deletion
   SET ESCAPE OFF && Pressing the ESC key interrupts program and command execution
   SET EXCLUSIVE OFF && Specifies that tables are opened for shared use on a network
   SET HOURS TO 12 && Sets the system clock to a 12-hour time format
   SET MULTILOCKS ON && Required for row or table buffering and allows multiple records to be locked using LOCK( ) or RLOCK( )
   SET REFRESH TO 5,3 && Frequency (in seconds) to update a browse window or memo editing window, or to refresh local memory buffers - 1st parameter is for local data, 2nd parameter is for network data
   SET REPORTBEHAVIOR 90 && Using the new reporting engine features
   _REPORTOUTPUT = "ReportOutput.app" && Designate application to use for report output
   _REPORTPREVIEW = "ReportPreview.app" && Designate application to use for report previewing
   SET REPROCESS TO 5 SECONDS && How long will Visual FoxPro attempt to lock a file or record after an unsuccessful locking attempt
   SET SECONDS OFF && Specifies that seconds are not displayed in the time portion of a DateTime value
   SET STATUS BAR ON && Displays the graphical status bar at the bottom of the _screen
   SET SYSMENU OFF && Turn off the default system menu that Visual FoxPro uses
   SET TALK OFF && Prevents talk from being sent to the main Visual FoxPro window, the system message window, the graphical status bar, or a user-defined window
   IF _VFP.STARTMODE = 0  && running inside the Visual FoxPro IDE
      lcPath = LEFT(SYS(16,0), RAT("\", SYS(16,0), 2))
      SET DEFAULT TO (lcPath) && Specifies the default drive and directory
      SET PATH TO (lcPath + ";Data\;Forms\;Help\;Images\;Libs\;Menus\;Progs\;Reports\") && Specifies a path for file searches
   ELSE
      lcPath = JUSTPATH(SYS(16,0))
      SET DEFAULT TO (lcPath) && Specifies the default drive and directory
      SET PATH TO (lcPath + "Data\;Help\;Images\") && Specifies a path for file searches
   ENDIF
ENDPROC

********************
PROCEDURE SetupScreen
********************
   _SCREEN.WINDOWSTATE = 2
   IF _VFP.STARTMODE = 0
      _SCREEN.TAG = _SCREEN.CAPTION && Save _Screen's Caption so it can later be restored
   ENDIF
   *_SCREEN.CAPTION = "Change Caption"
*!* Personal preference to have the clientpath and the datapath available as _screen properties
   _SCREEN.ADDPROPERTY("ClientPath", ADDBS(SYS(5) + SYS(2003)))
*!* If data is not local, path would be pulled from an INI or Registry
   _SCREEN.ADDPROPERTY("DataPath", ADDBS(SYS(5) + SYS(2003)) + "Data\")
ENDPROC

********************
PROCEDURE SetupMenu
********************
*!* Bring up our user-defined menu
   *DO Menu1.MPR
ENDPROC

********************
PROCEDURE SetupDatabase
********************
*!* Open and set the database
   OPEN DATABASE (_SCREEN.datapath + "reylin.dbc")
   SET DATABASE TO reylin
ENDPROC

********************
PROCEDURE ProperShutdown
********************
   LOCAL loForm

   ON SHUTDOWN && Must shut off the quit routine otherwise it will fire recursively
*!* Code to clean up would go here such as releasing resources and closing databases

   CLEAR EVENTS
   RELEASE ALL   
  
   IF _VFP.STARTMODE = 0 && running inside the Visual FoxPro IDE
      REMOVEPROPERTY(_SCREEN, "clientpath")
      REMOVEPROPERTY(_SCREEN, "datapath")
      SET SYSMENU TO DEFAULT
      ON ERROR && Restore default Error Handling
   ENDIF
   
    *!* Close any open forms
   loForm = .NULL. && Not necessary, but force of habit
   FOR EACH loForm IN _SCREEN.FORMS
      loForm.RELEASE()
   NEXT
   
   CLOSE DATABASES ALL && closes any open tables and database
   CLEAR ALL && Clear all remaingin items from memory

   IF _VFP.STARTMODE = 0
      _SCREEN.CAPTION = _SCREEN.TAG && Restore _Screen's Caption
      _SCREEN.TAG = ""
      CANCEL
   ELSE
     QUIT
   ENDIF
ENDPROC
