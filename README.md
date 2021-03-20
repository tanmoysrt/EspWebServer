<p style="color: red; font-weight: bold">>>>>>  gd2md-html alert:  ERRORs: 0; WARNINGs: 0; ALERTS: 8.</p>
<ul style="color: red; font-weight: bold"><li>See top comment block for details on ERRORs and WARNINGs. <li>In the converted Markdown or HTML, search for inline alerts that start with >>>>>  gd2md-html alert:  for specific instances that need correction.</ul>

<p style="color: red; font-weight: bold">Links to alert messages:</p><a href="#gdcalert1">alert1</a>
<a href="#gdcalert2">alert2</a>
<a href="#gdcalert3">alert3</a>
<a href="#gdcalert4">alert4</a>
<a href="#gdcalert5">alert5</a>
<a href="#gdcalert6">alert6</a>
<a href="#gdcalert7">alert7</a>
<a href="#gdcalert8">alert8</a>

<p style="color: red; font-weight: bold">>>>>> PLEASE check and correct alert issues and delete this message and the inline alerts.<hr></p>


**Student Auto Attendance System by RFID Card**

**&**

** Anti-Escape system **

**_<span style="text-decoration:underline;">Target :</span>_**



*   Make Easy The Process of Attendance
*   Alert Guardians About When Student Got Entered and Left The School
*   Prohibit and Generate Report about School Escape Of Students
*   Sometimes guardians are not aware that in spite of going to school his son/daughter has gone to another place or may have escaped from school. So the guardians will be alerted and school has a complete details of those students 
*   School Administration can download attendance data directly from the admin panel.

**_<span style="text-decoration:underline;">Features : </span>_**



*   When any student enters the student will be marked as present and his/her guardian will receive a message about that.



<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image1.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image1.jpg "image_tooltip")




*   When any student will leave the school that will be recorded and the guardian will get a sms with the timestamp.

    

<p id="gdcalert2" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image2.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert3">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image2.jpg "image_tooltip")


*   If any student doesn't come to school , their guardians will be alerted that he hasn’t come to school today.

    

<p id="gdcalert3" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image3.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert4">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image3.jpg "image_tooltip")


*   If any student has given attendance and haven’t left the school . That indicates that he may have escaped from school through any secret path. So, after a specified time , an automated script will find those students and will initiate sms to their guardians about that. 



<p id="gdcalert4" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image4.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert5">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image4.jpg "image_tooltip")



<p id="gdcalert5" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: Definition &darr;&darr; outside of definition list. Missing preceding term(s)? </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert6">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


**: Diagram of System : **



<p id="gdcalert6" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image5.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert7">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image5.png "image_tooltip")


Source code of server Side : [https://github.com/Tanmoy741127/EspWebServer](https://github.com/Tanmoy741127/EspWebServer)

Source code of nodemcu client side : [https://github.com/Tanmoy741127/EspWebServer/blob/main/Nodemcu%20Code/espclient.ino](https://github.com/Tanmoy741127/EspWebServer/blob/main/Nodemcu%20Code/espclient.ino)

Video Link :

 [https://drive.google.com/file/d/1ylXWKrQs0f4XyNFerL_ih68Nub8nMsmH/view](https://drive.google.com/file/d/1ylXWKrQs0f4XyNFerL_ih68Nub8nMsmH/view)

**_** For security purposes, the api keys & credentials has been wiped in code _**

In the submitted video , this timetable has been configured in server(to show the experiment in short span of time) ---


<table>
  <tr>
   <td>4:45pm on or before
   </td>
   <td>Normal Time to enter school
   </td>
  </tr>
  <tr>
   <td>4:50pm on or after 
   </td>
   <td>Send Notifications to Parents of students who haven't come school
   </td>
  </tr>
  <tr>
   <td>4:55pm on or before
   </td>
   <td>School has finished
   </td>
  </tr>
  <tr>
   <td>5:00pm on or after
   </td>
   <td>Time to check those who have entered school but haven't exited through gates .
   </td>
  </tr>
</table>


**Students Data (Name , Class, Roll No, Card Id, Phone No, Total Attendance )**



<p id="gdcalert7" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image6.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert8">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image6.png "image_tooltip")


**<span style="text-decoration:underline;">Students Attendance Data</span>**



<p id="gdcalert8" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image7.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert9">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image7.png "image_tooltip")
