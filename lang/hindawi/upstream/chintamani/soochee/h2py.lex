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
_a_nnu                       {printf("{");}
poor_nna                       {printf("}");}
tipa                       {printf("//");}
mukhya                      {printf("main");}
                           /*keywords*/
saara                        {printf("abstract");}
_dwaaphala                    {printf("boolean");}
_awaroa_dha                   {printf("break");}
baa_eeta                       {printf("byte");}
_haala                       {printf("case");}
paka_rdoa                     {printf("catch");}
_akxara                      {printf("char");}
shraee_nnee                       {printf("class");}
s_thira                      {printf("const");}
jaaree                       {printf("continue");}
shaeexa                       {printf("default");}
karoa                       {printf("do");}
_dwiguna                   {printf("double");}
_anya_thaa                    {printf("else");}
poorwaja                     {printf("extends");}
_an_tima                    {printf("final");}
_an_tima_ta_hh                  {printf("finally");}
bhagna                      {printf("float");}
krama                       {printf("for");}
jaa_oa                       {printf("goto");}
_agara                      {printf("if");}
laagu                       {printf("implements");}
_aayaa_ta                     {printf("import");}
_awa_taara                    {printf("instanceof");}
poor_nnaa_mka                       {printf("int");}
swaroopa                     {printf("interface");}
_deergha                       {printf("long");}
yaa_m_trika                     {printf("native");}
nayaa                       {printf("new");}
koaxa                       {printf("package");}
nijee                      {printf("private");}
rakxi_ta                     {printf("protected");}
khulaa                       {printf("public");}
waapasa                     {printf("return");}
laghu                       {printf("short");}
ja_rda                        {printf("static");}
_d_ri_rdhabhagna                    {printf("strictfp");}
ma_ha                        {printf("super");}
chayana                     {printf("switch");}
samaprawaa_ha                  {printf("synchronised");}
ya_ha                        {printf("this");}
phaee_mkoa                       {printf("throw");}
phaee_mka_taa__hai             {printf("throws");}
_as_thaayee                    {printf("transient");}
prayaasa                     {printf("try");}
wyoama                      {printf("void");}
_as_thira                     {printf("volatile");}
jaba_taka                   {printf("while");}
 
prayoaga_shraee_nnee           {printf("Applet");}
prayoaga                  {printf("applet");}
_tarka                    {printf("args");}
ga_nni_ta__truti            {printf("ArithmeticException");}
wyoo_ha_soochakaa_mka_khaee_da__truti   {printf("ArrayIndexOutOfBoundsException");}
wyoo_ha_s_thi_ti__truti         {printf("ArrayStateException");}
_dhwani__a_msha               {printf("AudioClip");}
_ousa_mkha                   {printf("awt");} /* _oujzaara sa_mkxip_ta khi_rdakee*/
baphara_paathaka                {printf("BufferedReader");}
_akxara_s_thaana                 {printf("charAt");}
shraee_nnee_saa_nachaa__truti               {printf("ClassCastException");}
shraee_nnee__upalab_dha_na_hee_m__truti      {printf("ClassNotFoundException");}
shraee_nnee_niraa_dhaara__truti              {printf("ClassNotSupportedException");}
nakala                      {printf("clone");}
ba_m_da                      {printf("close");}
bhaee_da                      {printf("compareTo");}
sa_myoaga                    {printf("concat");}
ya_ha_ka_rdee                  {printf("currentThread");}
_dina                      {printf("Date");}
mitaa_oa                    {printf("destroy");}
maalaa_likhoa                {printf("drawString");}
_a_m_ta_maee_m                  {printf("endsWith");}
baraabara                    {printf("equals");}
baraabara_na                  {printf("equalsIgnoreCase");}
khaa_taa_prawaeesha_prawaa_ha       {printf("FileInputStream");}
khaa_taa_nikaasa_prawaa_ha        {printf("FileOutputStream");}
bharoa_dhaeera                  {printf("fillInStackTrace");}
_a_m_tima                    {printf("finalize");}
loa__dhwani__a_msha             {printf("getAudioClip");}
loa_baa_ita                  {printf("getBytes");}
loa__akxara                 {printf("getChars");}
loa_shraee_nnee                {printf("getClass");}
loa__a_msha_maapa               {printf("getContentLength");}
loa__a_msha_prakaara            {printf("getContentType");}
loa__dina                   {printf("getDate");}
loa__an_ta                  {printf("getExpiration");}
loa_kxaee_tra_soochakaa_mka      {printf("GetFieldID");}
loa_chhawi                   {printf("getImage");}
loa_prawaeesha_prawaa_ha         {printf("getInputStream");}
loa_poor_nna_kxaee_tra         {printf("GetIntField");}
loa_poorwa_ba_dalee            {printf("getLastModified");}
loa_s_thaaneeya_sa_m_daeesha        {printf("getLocalizedMessage");}
loa_sa_mkaee_ta                 {printf("getMessage");}
loa_naama                   {printf("getName");}
loa_was_tu_shraee_nnee          {printf("GetObjectClass");}
loa__tarka                  {printf("getParameter");}
loa_praa_thamika              {printf("getPriority");}
chi_traa_mkana                {printf("Graphics");}
_haisha_koota                  {printf("hashCode");}
_awai_dha_prawaeesha__truti            {printf("IllegalAccessException");}
_awai_dha__tarka__truti             {printf("IllegalArgumentException");}
_awai_dha_yoajaka__truti              {printf("IllegalMonitorStateException");}
_awai_dha_s_thi_ti__truti            {printf("IllegalStateException");}
_awai_dha_ka_rdee_s_thi_ti__truti       {printf("IllegalThreadStateException");}
chhawi                      {printf("Image");}
soochakaa_mka                  {printf("indexOf");}
soochakaa_mka_bhaee_da__truti      {printf("IndexOutOfBoundsException");}
_upasarga                   {printf("init");}
prawaeesha_prawaa_ha            {printf("InputStream");}
prawaeesha_prawaa_ha_paathaka       {printf("InputStreamReader");}
_awa_taara_nna__truti            {printf("InstantiationException");}
wighna__truti             {printf("InterruptedException");}
pana                       {printf("io");}
jeewi_ta__hai                 {printf("isAlive");}
k_ri_trima                  {printf("java");}
maeela                      {printf("join");}
poorwa_soochakaa_mka           {printf("lastIndexOf");}
maapa                      {printf("length");}
loa_koaxa                   {printf("loadLibrary");}
_doa_haraa_oa                   {printf("loop");}
ga_nni_ta                     {printf("Math");}
_uchcha_praa_thamika_taa          {printf("MAX_PRIORITY");}
nyoona_praa_thamika_taa         {printf("MIN_PRIORITY");}
_ri_nna_wyoo_ha_maapa__truti     {printf("NegativeArraySizeException");}
naeeta                      {printf("net");}
_agalaa__dwi                {printf("nextdouble");}
saamaanya_praa_thamika_taa      {printf("NORM_PRIORITY");}
koa_ee__aisaa_kxaee_tra_na_hee_m__truti     {printf("NoSuchFieldException");}
koa_ee__aisee_kriyaa_na_hee_m__truti       {printf("NoSuchMethodException");}
sa_mkaee_ta                    {printf("notify");}
sa_mkaee_ta_saba                 {printf("notifyAll");}
shoonya_soochaka__truti      {printf("NullPointerException");}
_a_mka_rachanaa-_truti          {printf("NumberFormatException");}
was_tu                    {printf("Object");}
khoaloa_samban_dha             {printf("openConnection");}
baa_hara                     {printf("out");}
nikaasa_prawaa_ha             {printf("OutputStream");}
banaa_oa                     {printf("paint");}
bajaa_oa                     {printf("play");}
ma_likhoa_na                 {printf("println");}
_dikhaa_oa_dhaeera                {printf("printStackTrace");}
chhaapaakaara                  {printf("PrintWriter");}
_akrama                    {printf("rand");}
ma_pa_rdhoa                   {printf("read");}
paathaka                     {printf("Reader");}
pa_mk_ti_pa_rdhoa              {printf("readLine");}
kxaee_tra_maeela              {printf("regionMatches");}
pra_tis_thaapana              {printf("replace");}
puna_hh__aarambha               {printf("resume");}
_aarambha                  {printf("run");}
_aarambha_laayaka                {printf("Runnable");}
surakxaa__truti            {printf("SecurityException");}
rakhoa_poor_nna_kxaee_tra         {printf("SetIntField");}
rakhoa_naama                  {printf("setName");}
rakhoa_praa_thamika_taa            {printf("setPriority");}
soa_jaa_oa                    {printf("sleep");}
warga_moola                 {printf("sqrt");}
shuroo                     {printf("start");}
shuroo_maee_m                  {printf("startsWith");}
wiraama                     {printf("stop");}
maalaa_shraee_nnee             {printf("String");}
maalaa_baphara                  {printf("StringBuffer");}
maalaa_soochakaa_mka_seemaa_khaee_da     {printf("StringIndexOutOfBounds");}
_upamaalaa                    {printf("substring");}
s_thagi_ta                    {printf("suspend");}
pra_nnaalee                   {printf("System");}
ka_rdee                      {printf("Thread");}
phaee_mkanaee_laayaka               {printf("Throwable");}
karoa__akxara_wyoo_ha            {printf("toCharArray");}
karoa_chhoataee                  {printf("toLowerCase");}
karoa_maalaa                  {printf("toString");}
karoa_ba_rdaee                  {printf("toUpperCase");}
chhaa_natoa                     {printf("trim");}
kriyaa__upalab_dha_na_hee_m__truti      {printf("UnsupportedOperationException");}
nayaa__haala                   {printf("update");}
wasa_mj_yna                     {printf("URL");} /* wyaapaka sroa_ta j_ynaa_taka */
wasa_mj_yna_samban_dha       {printf("URLConnection");}
_upayoaga                     {printf("util");}
maana                       {printf("valueof");}
rukoa                      {printf("wait");}
ma_likhoa                      {printf("write");}
laeekhaka                      {printf("Writer");}
 
%%
