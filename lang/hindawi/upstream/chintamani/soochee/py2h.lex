%{
/*
Copyright (C) 2003,2004,2005,2006 Abhishek Choudhary
This file is part of the Hindawi Indic Programming System.

The Hindawi Indic Programming Systemis free software; 
you can redistribute it and/or modify it under the terms of the 
GNU General Public License as published by the 
Free Software Foundation; either version 2 of the License, or 
(at your option) any later version.

The Hindawi Indic Programming System is distributed in the hope 
that it will be useful, but WITHOUT ANY WARRANTY; without 
even the implied warranty of MERCHANTABILITY or FITNESS FOR 
A PARTICULAR PURPOSE. See the GNU General Public License for 
more details.

You should have received a copy of the GNU General Public
License along with this file; see the file COPYING. If
not, write to the Free Software Foundation,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
*/

/*
Modifications: (Please maintain reverse chronological order)

	dd-mmm-yyyy, Nature of modification,
                        Name of modifier <alias>,
			email adress of modifier

        31-Jul-2006, Added the modifications section,
                        Abhishek Choudhary <hi_pedler>,
                        choudhary@indicybers.net

End of modifications.
*/

%}


%%

\'("\\\'"|.*)*\'                       {printf("%s",yytext);}
\"("\\\""|[^\"^\n]*)*\"                {printf("%s",yytext);}                                                                  
\{         {printf("¤Áİ");}
\}         {printf("ÈŞÏèÁ");}
\/\/         {printf("½ÛÈ");}
main         {printf("Ìİ´èÍ");}
abstract         {printf("×ÚÏ");}
boolean         {printf("ÄèÔÚÉÑ");}
break         {printf("¤ÔÏåÅ");}
byte         {printf("ÊÚ§½");}
case         {printf("ØÚÑ");}
catch         {printf("È³¿éå");}
char         {printf("¤³èÖÏ");}
class         {printf("ÕèÏáÁÜ");}
const         {printf("×èÃÛÏ");}
continue         {printf("ºÚÏÜ");}
default         {printf("ÕáÖ");}
do         {printf("³Ïå");}
double         {printf("ÄèÔÛµİÆ");}
else         {printf("¤ÆèÍÃÚ");}
extends         {printf("ÈŞÏèÔº");}
final         {printf("¤ÆèÂÛÌ");}
finally         {printf("¤ÆèÂÛÌÂ£");}
float         {printf("ËµèÆ");}
for         {printf("³èÏÌ");}
goto         {printf("ºÚ°");}
if         {printf("¤µÏ");}
implements         {printf("ÑÚµİ");}
import         {printf("¥ÍÚÂ");}
instanceof         {printf("¤ÔÂÚÏ");}
int         {printf("ÈŞÏèÁÚ¢³");}
interface         {printf("×èÔÏŞÈ");}
long         {printf("ÄÜÏè¶");}
native         {printf("ÍÚ¢ÂèÏÛ³");}
new         {printf("ÆÍÚ");}
package         {printf("³åÖ");}
private         {printf("ÆÛºÜ");}
protected         {printf("Ï³èÖÛÂ");}
public         {printf("´İÑÚ");}
return         {printf("ÔÚÈ×");}
short         {printf("Ñ¶İ");}
static         {printf("º¿é");}
strictfp         {printf("ÄßÀéËµèÆ");}
super         {printf("ÌØ");}
switch         {printf("¸ÍÆ");}
synchronised         {printf("×ÌÈèÏÔÚØ");}
this         {printf("ÍØ");}
throw         {printf("Éá¢³å");}
throws         {printf("Éá¢³ÂÚ_Øâ");}
transient         {printf("¤×èÃÚÍÜ");}
try         {printf("ÈèÏÍÚ×");}
void         {printf("ÔèÍåÌ");}
volatile         {printf("¤×èÃÛÏ");}
while         {printf("ºÊÂ³");}
Applet         {printf("ÈèÏÍåµ_ÕèÏáÁÜ");}
applet         {printf("ÈèÏÍåµ");}
args         {printf("ÂÏè³");}
ArithmeticException         {printf("µÁÛÂ_ÂèÏİ½Û");}
ArrayIndexOutOfBoundsException         {printf("ÔèÍŞØ_×Ş¸³Ú¢³_´áÄ_ÂèÏİ½Û");}
ArrayStateException         {printf("ÔèÍŞØ_×èÃÛÂÛ_ÂèÏİ½Û");}
AudioClip         {printf("ÅèÔÆÛ_¤¢Õ");}
awt         {printf("±×¢´");}
BufferedReader         {printf("ÊÉÏ_ÈÚ¾³");}
charAt         {printf("¤³èÖÏ_×èÃÚÆ");}
ClassCastException         {printf("ÕèÏáÁÜ_×Ú¡¸Ú_ÂèÏİ½Û");}
ClassNotFoundException         {printf("ÕèÏáÁÜ_¨ÈÑÊèÅ_ÆØÜ¢_ÂèÏİ½Û");}
ClassNotSupportedException         {printf("ÕèÏáÁÜ_ÆÛÏÚÅÚÏ_ÂèÏİ½Û");}
clone         {printf("Æ³Ñ");}
close         {printf("Ê¢Ä");}
compareTo         {printf("ËáÄ");}
concat         {printf("×¢Íåµ");}
currentThread         {printf("ÍØ_³¿éÜ");}
Date         {printf("ÄÛÆ");}
destroy         {printf("ÌÛ½Ú°");}
drawString         {printf("ÌÚÑÚ_ÑÛ´å");}
endsWith         {printf("¤¢Â_Ìá¢");}
equals         {printf("ÊÏÚÊÏ");}
equalsIgnoreCase         {printf("ÊÏÚÊÏ_Æ");}
FileInputStream         {printf("´ÚÂÚ_ÈèÏÔáÕ_ÈèÏÔÚØ");}
FileOutputStream         {printf("´ÚÂÚ_ÆÛ³Ú×_ÈèÏÔÚØ");}
fillInStackTrace         {printf("ËÏå_ÀáÏ");}
finalize         {printf("¤¢ÂÛÌ");}
getAudioClip         {printf("Ñå_ÅèÔÆÛ_¤¢Õ");}
getBytes         {printf("Ñå_ÊÚ¦½");}
getChars         {printf("Ñå_¤³èÖÏ");}
getClass         {printf("Ñå_ÕèÏáÁÜ");}
getContentLength         {printf("Ñå_¤¢Õ_ÌÚÈ");}
getContentType         {printf("Ñå_¤¢Õ_ÈèÏ³ÚÏ");}
getDate         {printf("Ñå_ÄÛÆ");}
getExpiration         {printf("Ñå_¤ÆèÂ");}
GetFieldID         {printf("Ñå_³èÖáÂèÏ_×Ş¸³Ú¢³");}
getImage         {printf("Ñå_¹ÔÛ");}
getInputStream         {printf("Ñå_ÈèÏÔáÕ_ÈèÏÔÚØ");}
GetIntField         {printf("Ñå_ÈŞÏèÁ_³èÖáÂèÏ");}
getLastModified         {printf("Ñå_ÈŞÏèÔ_ÊÄÑÜ");}
getLocalizedMessage         {printf("Ñå_×èÃÚÆÜÍ_×¢ÄáÕ");}
getMessage         {printf("Ñå_×¢³áÂ");}
getName         {printf("Ñå_ÆÚÌ");}
GetObjectClass         {printf("Ñå_Ô×èÂİ_ÕèÏáÁÜ");}
getParameter         {printf("Ñå_ÂÏè³");}
getPriority         {printf("Ñå_ÈèÏÚÃÌÛ³");}
Graphics         {printf("¸ÛÂèÏÚ¢³Æ");}
hashCode         {printf("ØâÕ_³Ş½");}
IllegalAccessException         {printf("¤ÔâÅ_ÈèÏÔáÕ_ÂèÏİ½Û");}
IllegalArgumentException         {printf("¤ÔâÅ_ÂÏè³_ÂèÏİ½Û");}
IllegalMonitorStateException         {printf("¤ÔâÅ_Íåº³_ÂèÏİ½Û");}
IllegalStateException         {printf("¤ÔâÅ_×èÃÛÂÛ_ÂèÏİ½Û");}
IllegalThreadStateException         {printf("¤ÔâÅ_³¿éÜ_×èÃÛÂÛ_ÂèÏİ½Û");}
Image         {printf("¹ÔÛ");}
indexOf         {printf("×Ş¸³Ú¢³");}
IndexOutOfBoundsException         {printf("×Ş¸³Ú¢³_ËáÄ_ÂèÏİ½Û");}
init         {printf("¨È×Ïèµ");}
InputStream         {printf("ÈèÏÔáÕ_ÈèÏÔÚØ");}
InputStreamReader         {printf("ÈèÏÔáÕ_ÈèÏÔÚØ_ÈÚ¾³");}
InstantiationException         {printf("¤ÔÂÚÏÁ_ÂèÏİ½Û");}
InterruptedException         {printf("ÔÛ¶èÆ_ÂèÏİ½Û");}
io         {printf("ÈÆ");}
isAlive         {printf("ºÜÔÛÂ_Øâ");}
java         {printf("³ßÂèÏÛÌ");}
join         {printf("ÌáÑ");}
lastIndexOf         {printf("ÈŞÏèÔ_×Ş¸³Ú¢³");}
length         {printf("ÌÚÈ");}
loadLibrary         {printf("Ñå_³åÖ");}
loop         {printf("ÄåØÏÚ°");}
Math         {printf("µÁÛÂ");}
MAX_PRIORITY         {printf("¨¸è¸_ÈèÏÚÃÌÛ³ÂÚ");}
MIN_PRIORITY         {printf("ÆèÍŞÆ_ÈèÏÚÃÌÛ³ÂÚ");}
NegativeArraySizeException         {printf("ªÁ_ÔèÍŞØ_ÌÚÈ_ÂèÏİ½Û");}
net         {printf("Æá½");}
nextdouble         {printf("¤µÑÚ_ÄèÔÛ");}
NORM_PRIORITY         {printf("×ÚÌÚÆèÍ_ÈèÏÚÃÌÛ³ÂÚ");}
NoSuchFieldException         {printf("³å§_­×Ú_³èÖáÂèÏ_ÆØÜ¢_ÂèÏİ½Û");}
NoSuchMethodException         {printf("³å§_­×Ü_³èÏÛÍÚ_ÆØÜ¢_ÂèÏİ½Û");}
notify         {printf("×¢³áÂ");}
notifyAll         {printf("×¢³áÂ_×Ê");}
NullPointerException         {printf("ÕŞÆèÍ_×Ş¸³_ÂèÏİ½Û");}
NumberFormatException         {printf("¤¢³_Ï¸ÆÚ-ÂèÏİ½Û");}
Object         {printf("Ô×èÂİ");}
openConnection         {printf("´åÑå_×ÌèÊÆèÅ");}
out         {printf("ÊÚØÏ");}
OutputStream         {printf("ÆÛ³Ú×_ÈèÏÔÚØ");}
paint         {printf("ÊÆÚ°");}
play         {printf("ÊºÚ°");}
println         {printf("Ì_ÑÛ´å_Æ");}
printStackTrace         {printf("ÄÛ´Ú°_ÀáÏ");}
PrintWriter         {printf("¹ÚÈÚ³ÚÏ");}
rand         {printf("¤³èÏÌ");}
read         {printf("Ì_ÈÀéå");}
Reader         {printf("ÈÚ¾³");}
readLine         {printf("È¢³èÂÛ_ÈÀéå");}
regionMatches         {printf("³èÖáÂèÏ_ÌáÑ");}
replace         {printf("ÈèÏÂÛ×èÃÚÈÆ");}
resume         {printf("ÈİÆ£_¥ÏÌèË");}
run         {printf("¥ÏÌèË");}
Runnable         {printf("¥ÏÌèË_ÑÚÍ³");}
SecurityException         {printf("×İÏ³èÖÚ_ÂèÏİ½Û");}
SetIntField         {printf("Ï´å_ÈŞÏèÁ_³èÖáÂèÏ");}
setName         {printf("Ï´å_ÆÚÌ");}
setPriority         {printf("Ï´å_ÈèÏÚÃÌÛ³ÂÚ");}
sleep         {printf("×å_ºÚ°");}
sqrt         {printf("ÔÏèµ_ÌŞÑ");}
start         {printf("ÕİÏŞ");}
startsWith         {printf("ÕİÏŞ_Ìá¢");}
stop         {printf("ÔÛÏÚÌ");}
String         {printf("ÌÚÑÚ_ÕèÏáÁÜ");}
StringBuffer         {printf("ÌÚÑÚ_ÊÉÏ");}
StringIndexOutOfBounds         {printf("ÌÚÑÚ_×Ş¸³Ú¢³_×ÜÌÚ_´áÄ");}
substring         {printf("¨ÈÌÚÑÚ");}
suspend         {printf("×èÃµÛÂ");}
System         {printf("ÈèÏÁÚÑÜ");}
Thread         {printf("³¿éÜ");}
Throwable         {printf("Éá¢³Æá_ÑÚÍ³");}
toCharArray         {printf("³Ïå_¤³èÖÏ_ÔèÍŞØ");}
toLowerCase         {printf("³Ïå_¹å½á");}
toString         {printf("³Ïå_ÌÚÑÚ");}
toUpperCase         {printf("³Ïå_Ê¿éá");}
trim         {printf("¹Ú¡½å");}
UnsupportedOperationException         {printf("³èÏÛÍÚ_¨ÈÑÊèÅ_ÆØÜ¢_ÂèÏİ½Û");}
update         {printf("ÆÍÚ_ØÚÑ");}
URL         {printf("Ô×¢ºè¼");}
URLConnection         {printf("Ô×¢ºè¼_×ÌèÊÆèÅ");}
util         {printf("¨ÈÍåµ");}
valueof         {printf("ÌÚÆ");}
wait         {printf("Ïİ³å");}
write         {printf("Ì_ÑÛ´å");}
Writer         {printf("Ñá´³");}

%%

