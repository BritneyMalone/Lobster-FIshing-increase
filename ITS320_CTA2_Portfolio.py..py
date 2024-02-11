#Program name: 

ods html5 (id=web) style=daisy path="file-path"                 /*  */
          file="goal15_dd1_20230721.csv";

ods graphics / width=4.5in;                                     /*  */

title "Goal 15: Lobster Driving Growth in Fishery Exports";            /*  */
footnote "Data: WORK.IMPORT";

proc sgplot data=work.import (where=(type ne 'Hybrid'));       /*  */
   vbar type / response=mpg_highway                             /*  */
          stat=mean
          group=origin
          groupdisplay=cluster;
   yaxis label="Mean Highway MPG";                              /*  */
run;

title;                                                          /*  */
footnote;
ods graphics / reset;                                           /*  */
ods html5 (id=web) close;                                       /*  */
ods html5 (id=web) style=daisy path="file-path"                 /* 1 */
          file="file-name";

ods graphics / width=4.5in;                                     /* 2 */

title "Mean Highway MPG By Vehicle Type and Origin";            /* 3 */
footnote "Data: SASHELP.CARS";

proc sgplot data=sashelp.cars (where=(type ne 'Hybrid'));       /* 4 */
   vbar type / response=mpg_highway                             /* 5 */
          stat=mean
          group=origin
          groupdisplay=cluster;
   yaxis label="Mean Highway MPG";                              /* 6 */
run;

title;                                                          /* 7 */
footnote;
ods graphics / reset;                                           /* 8 */
ods html5 (id=web) close;   
