import random
import time
import math
import csv

payment_list = [] 

company_list = [
    { 'Del Monte Foods Co':  ['PO Box 1473+City+FL', 'PO Box 1390+City+TX', 'PO Box 8097+City+FL'] },
    { 'Dell Computer Corporation':  ['PO Box 4377+City+FL', 'PO Box 4312+City+KY', 'PO Box 2975+City+FL'] },
    { 'Delphi Corp':  ['PO Box 4329+City+KY', 'PO Box 44+City+WA', 'PO Box 1958+City+CA'] },
    { 'Delta Air Lines Inc':  ['PO Box 6551+City+VT', 'PO Box 9630+City+CT', 'PO Box 5851+City+CT'] },
    { 'Deluxe Corporation':  ['PO Box 2010+City+GA', 'PO Box 7849+City+CT', 'PO Box 4856+City+MI'] },
    { 'Devon Energy Corporation':  ['PO Box 8955+City+CO', 'PO Box 7421+City+CO', 'PO Box 7889+City+WA'] },
    { 'Di Giorgio Corporation':  ['PO Box 2186+City+CA', 'PO Box 3212+City+CT', 'PO Box 3855+City+FL'] },
    { 'Dial Corporation':  ['PO Box 4651+City+NY', 'PO Box 1057+City+MO', 'PO Box 4873+City+GA'] },
    { 'Diebold Incorporated':  ['PO Box 4226+City+VT', 'PO Box 9693+City+FL', 'PO Box 8080+City+FL'] },
    { 'Dillards Inc':  ['PO Box 2261+City+FL', 'PO Box 3826+City+WA', 'PO Box 222+City+KY'] },
    { 'DIMON Incorporated':  ['PO Box 9503+City+WA', 'PO Box 7192+City+GA', 'PO Box 7239+City+KY'] },
    { 'Dole Food Company Inc':  ['PO Box 1535+City+FL', 'PO Box 3975+City+KY', 'PO Box 8095+City+TX'] },
    { 'Dollar General Corporation':  ['PO Box 8813+City+CA', 'PO Box 5750+City+CO', 'PO Box 6023+City+NY'] },
    { 'Dollar Tree Stores Inc':  ['PO Box 1201+City+FL', 'PO Box 621+City+WA', 'PO Box 6588+City+WA'] },
    { 'Dominion Resources Inc':  ['PO Box 5247+City+FL', 'PO Box 1475+City+NY', 'PO Box 8355+City+KY'] },
    { 'Dominos Pizza LLC':  ['PO Box 6703+City+CT', 'PO Box 3674+City+VT', 'PO Box 5127+City+MI'] },
    { 'Dover Corporation Inc':  ['PO Box 5452+City+WA', 'PO Box 640+City+MI', 'PO Box 365+City+VT'] },
    { 'Dow Chemical Company':  ['PO Box 6748+City+CA', 'PO Box 3083+City+KY', 'PO Box 9410+City+NY'] },
    { 'Dow Jones & Company Inc':  ['PO Box 4947+City+MO', 'PO Box 7844+City+TX', 'PO Box 5374+City+KY'] },
    { 'DPL Inc':  ['PO Box 3749+City+NY', 'PO Box 4028+City+GA', 'PO Box 6007+City+CO'] },
    { 'DQE Inc':  ['PO Box 2520+City+WA', 'PO Box 3749+City+MO', 'PO Box 526+City+MO'] },
    { 'Dreyers Grand Ice Cream Inc':  ['PO Box 3223+City+CA', 'PO Box 5389+City+CO', 'PO Box 6139+City+FL'] },
    { 'DST Systems Inc':  ['PO Box 1150+City+CO', 'PO Box 9232+City+TX', 'PO Box 5359+City+VT'] },
    { 'DTE Energy Co':  ['PO Box 1597+City+CO', 'PO Box 5178+City+NY', 'PO Box 8550+City+KY'] },
    { 'EI Du Pont de Nemours and Company':  ['PO Box 8834+City+NY', 'PO Box 110+City+GA', 'PO Box 379+City+KY'] },
    { 'Duke Energy Corp':  ['PO Box 5215+City+GA', 'PO Box 1542+City+VT', 'PO Box 6033+City+CA'] },
    { 'Dun & Bradstreet Inc':  ['PO Box 4014+City+CO', 'PO Box 9509+City+VT', 'PO Box 3561+City+TX'] },
    { 'DURA Automotive Systems Inc':  ['PO Box 8055+City+MO', 'PO Box 4494+City+FL', 'PO Box 3208+City+MI'] },
    { 'DynCorp':  ['PO Box 6468+City+FL', 'PO Box 140+City+CA', 'PO Box 8835+City+GA'] },
    { 'Dynegy Inc':  ['PO Box 3772+City+FL', 'PO Box 9891+City+VT', 'PO Box 2323+City+CT'] },
    { 'E*Trade Group Inc':  ['PO Box 706+City+MO', 'PO Box 1278+City+KY', 'PO Box 4872+City+CT'] },
    { 'EW Scripps Company':  ['PO Box 3335+City+FL',' PO Box 3675+City+VT', 'PO Box 9725+City+CA'] },
    { 'Earthlink Inc':  ['PO Box 8113+City+CO', 'PO Box 2974+City+GA', 'PO Box 4816+City+KY'] },
    { 'Eastman Chemical Company':  ['PO Box 2742+City+CA', 'PO Box 9383+City+CO', 'PO Box 8579+City+CT'] },
    { 'Eastman Kodak Company':  ['PO Box 8510+City+MI', 'PO Box 5337+City+FL', 'PO Box 5191+City+CO'] },
    { 'Eaton Corporation':  ['PO Box 5955+City+VT', 'PO Box 2268+City+CO', 'PO Box 3697+City+WA'] },
    { 'Echostar Communications Corporation':  ['PO Box 6952+City+NY', 'PO Box 9391+City+CO', 'PO Box 1321+City+WA'] },
    { 'Ecolab Inc':  ['PO Box 9736+City+MI', 'PO Box 4558+City+GA', 'PO Box 7579+City+CT'] },
    { 'Edison International':  ['PO Box 9468+City+CT', 'PO Box 1042+City+NY', 'PO Box 5828+City+VT'] },
    { 'EGL Inc':  ['PO Box 6620+City+TX', 'PO Box 943+City+MO', 'PO Box 8351+City+MO'] },
    { 'El Paso Corporation':  ['PO Box 2668+City+FL', 'PO Box 9566+City+WA', 'PO Box 5390+City+MI'] },
    { 'Electronic Arts Inc':  ['PO Box 9359+City+CT', 'PO Box 4289+City+VT', 'PO Box 4691+City+GA'] },
    { 'Electronic Data Systems Corp':  ['PO Box 5682+City+KY', 'PO Box 4337+City+VT', 'PO Box 5562+City+NY'] },
    { 'Eli Lilly and Company':  ['PO Box 1828+City+CT', 'PO Box 2921+City+GA', 'PO Box 377+City+CA'] },
    { 'EMC Corporation':  ['PO Box 2765+City+MI', 'PO Box 2674+City+CA', 'PO Box 719+City+CT'] },
    { 'Emcor Group Inc':  ['PO Box 7176+City+TX', 'PO Box 638+City+CT', 'PO Box 9690+City+TX'] },
    { 'Emerson Electric Co':  ['PO Box 9883+City+MI', 'PO Box 8085+City+VT', 'PO Box 3246+City+VT'] },
    { 'Encompass Services Corporation':  ['PO Box 8480+City+MO', 'PO Box 5164+City+CA', 'PO Box 1729+City+MO'] },
    { 'Energizer Holdings Inc':  ['PO Box 6260+City+MI', 'PO Box 3624+City+FL', 'PO Box 2507+City+WA'] },
    { 'Energy East Corporation':  ['PO Box 2539+City+CO', 'PO Box 1712+City+FL', 'PO Box 8227+City+FL'] },
    { 'Engelhard Corporation':  ['PO Box 1112+City+MO', 'PO Box 5954+City+NY', 'PO Box 2800+City+CT'] },
    { 'Enron Corp':  ['PO Box 7258+City+KY', 'PO Box 3595+City+MI', 'PO Box 2554+City+FL'] },
    { 'Entergy Corporation':  ['PO Box 4700+City+CA', 'PO Box 7100+City+CA', 'PO Box 3675+City+WA'] },
    { 'Enterprise Products Partners LP':  ['PO Box 1298+City+NY', 'PO Box 9495+City+CT', 'PO Box 3606+City+MO'] },
    { 'EOG Resources Inc':  ['PO Box 5772+City+KY', 'PO Box 7839+City+GA', 'PO Box 4674+City+CO'] },
    { 'Equifax Inc':  ['PO Box 9748+City+MI', 'PO Box 2898+City+NY', 'PO Box 8358+City+CO'] },
    { 'Equitable Resources Inc':  ['PO Box 4159+City+TX', 'PO Box 1645+City+VT', 'PO Box 480+City+TX'] },
    { 'Equity Office Properties Trust':  ['PO Box 1556+City+MO', 'PO Box 6821+City+NY', 'PO Box 528+City+VT'] },
    { 'Equity Residential Properties Trust':  ['PO Box 9066+City+WA', 'PO Box 8788+City+VT', 'PO Box 9748+City+FL'] },
    { 'Estee Lauder Companies Inc':  ['PO Box 7416+City+CO', 'PO Box 1521+City+FL', 'PO Box 383+City+NY'] },
    { 'Exelon Corporation':  ['PO Box 8750+City+WA', 'PO Box 6325+City+KY', 'PO Box 8969+City+MI'] },
    { 'Exide Technologies':  ['PO Box 619+City+CO', 'PO Box 6718+City+CT', 'PO Box 9931+City+CO'] },
    { 'Expeditors International of Washington Inc':  ['PO Box 5762+City+VT',' PO Box 4372+City+WA', 'PO Box 4505+City+GA'] },
    { 'Express Scripts Inc':  ['PO Box 3544+City+MO', 'PO Box 8764+City+TX', 'PO Box 1102+City+TX'] },
    { 'ExxonMobil Corporation':  ['PO Box 7526+City+MO', 'PO Box 1017+City+CO', 'PO Box 665+City+NY'] },
    { 'Fairchild Semiconductor International Inc':  ['PO Box 9615+City+WA', 'PO Box 6520+City+MO', 'PO Box 5369+City+TX'] },
    { 'Family Dollar Stores Inc':  ['PO Box 1179+City+MO', 'PO Box 9493+City+MO', 'PO Box 3268+City+FL'] },
    { 'Farmland Industries Inc':  ['PO Box 3539+City+CA', 'PO Box 3674+City+KY', 'PO Box 1351+City+GA'] },
    { 'Federal Mogul Corp':  ['PO Box 9141+City+MO', 'PO Box 7214+City+TX', 'PO Box 90+City+CA'] },
    { 'Federated Department Stores Inc':  ['PO Box 2690+City+TX', 'PO Box 3190+City+MI', 'PO Box 9064+City+GA'] },
    { 'Federal Express Corp':  ['PO Box 2482+City+CO', 'PO Box 3100+City+MO', 'PO Box 986+City+FL'] },
    { 'Felcor Lodging Trust Inc':  ['PO Box 8433+City+CA', 'PO Box 5078+City+CO', 'PO Box 1166+City+MI'] },
    { 'Ferro Corp':  ['PO Box 6564+City+WA', 'PO Box 8422+City+KY', 'PO Box 7052+City+VT'] },
    { 'Fidelity National Financial Inc':  ['PO Box 2870+City+VT', 'PO Box 4771+City+MI', 'PO Box 2527+City+CO'] },
    { 'Fifth Third Bancorp':  ['PO Box 9043+City+TX', 'PO Box 3344+City+WA', 'PO Box 7068+City+KY'] },
    { 'First American Financial Corp':  ['PO Box 8034+City+TX', 'PO Box 5826+City+TX', 'PO Box 7097+City+TX'] },
    { 'First Data Corp':  ['PO Box 3398+City+CT', 'PO Box 6765+City+FL', 'PO Box 5857+City+KY'] },
    { 'First National of Nebraska Inc':  ['PO Box 8330+City+VT', 'PO Box 8948+City+CA', 'PO Box 7139+City+NY'] },
    { 'First Tennessee National Corp':  ['PO Box 5289+City+CO', 'PO Box 5192+City+FL', 'PO Box 2241+City+KY'] },
    { 'FirstEnergy Corp':  ['PO Box 8178+City+GA', 'PO Box 6012+City+MO', 'PO Box 3368+City+CA'] },
    { 'Fiserv Inc':  ['PO Box 731+City+WA', 'PO Box 2893+City+GA', 'PO Box 133+City+CO'] },
    { 'Fisher Scientific International Inc':  ['PO Box 2586+City+WA',' PO Box 2404+City+CT', 'PO Box 5517+City+NY'] },
    { 'FleetBoston Financial Co':  ['PO Box 4431+City+CO', 'PO Box 6557+City+CA', 'PO Box 8279+City+MI'] },
    { 'Fleetwood Enterprises Inc':  ['PO Box 1415+City+WA', 'PO Box 7084+City+MI', 'PO Box 8871+City+WA'] },
    { 'Fleming Companies Inc':  ['PO Box 5532+City+GA', 'PO Box 3903+City+CT', 'PO Box 318+City+NY'] },
    { 'Flowers Foods Inc':  ['PO Box 3203+City+CO', 'PO Box 4545+City+KY', 'PO Box 8494+City+MO'] },
    { 'Flowserv Corp':  ['PO Box 9556+City+MI', 'PO Box 5368+City+KY', 'PO Box 5655+City+NY'] },
    { 'Fluor Corp':  ['PO Box 6584+City+TX', 'PO Box 8657+City+CT', 'PO Box 9537+City+TX'] },
    { 'FMC Corp':  ['PO Box 7985+City+WA', 'PO Box 7062+City+CT', 'PO Box 3176+City+FL'] },
    { 'Foamex International Inc':  ['PO Box 2577+City+MO', 'PO Box 1690+City+MO', 'PO Box 1001+City+WA'] },
    { 'Foot Locker Inc':  ['PO Box 7411+City+WA', 'PO Box 4270+City+FL', 'PO Box 1071+City+MO'] },
    { 'Footstar Inc':  ['PO Box 1012+City+CA', 'PO Box 1312+City+MO', 'PO Box 5982+City+CA'] },
    { 'Ford Motor Co':  ['PO Box 4963+City+GA', 'PO Box 1243+City+GA', 'PO Box 2252+City+CO'] },
    { 'Forest Laboratories Inc':  ['PO Box 732+City+CO', 'PO Box 40+City+VT', 'PO Box 320+City+TX'] },
    { 'Fortune Brands Inc':  ['PO Box 3765+City+CA',' PO Box 9147+City+GA', 'PO Box 9914+City+FL'] },
    { 'Foster Wheeler Ltd':  ['PO Box 3080+City+WA', 'PO Box 7200+City+CA', 'PO Box 8702+City+CA'] },
    { 'FPL Group Inc':  ['PO Box 3716+City+CA', 'PO Box 3408+City+WA', 'PO Box 8447+City+FL'] },
    { 'Franklin Resources Inc':  ['PO Box 3276+City+KY', 'PO Box 4584+City+KY', 'PO Box 8066+City+NY'] },
    { 'Freeport McMoran Copper & Gold Inc':  ['PO Box 9606+City+KY', 'PO Box 7106+City+MO', 'PO Box 6576+City+TX'] },
    { 'Frontier Oil Corp':  ['PO Box 7229+City+MI', 'PO Box 3845+City+MI', 'PO Box 5262+City+NY'] },
    { 'Furniture Brands International Inc':  ['PO Box 2270+City+CA', 'PO Box 2717+City+KY', 'PO Box 8954+City+GA'] },
    { 'Gannett Co Inc':  ['PO Box 8880+City+FL', 'PO Box 7293+City+GA', 'PO Box 8486+City+WA'] },
    { 'Gap Inc':  ['PO Box 7394+City+TX', 'PO Box 9644+City+MO', 'PO Box 3353+City+FL'] },
    { 'Gateway Inc':  ['PO Box 8003+City+MO', 'PO Box 5438+City+CA', 'PO Box 3356+City+KY'] },
    { 'GATX Corporation':  ['PO Box 2372+City+VT', 'PO Box 1266+City+MI', 'PO Box 5388+City+TX'] },
    { 'Gemstar-TV Guide International Inc':  ['PO Box 3612+City+CT', 'PO Box 5246+City+FL', 'PO Box 8055+City+GA'] },
    { 'GenCorp Inc':  ['PO Box 3948+City+NY', 'PO Box 1390+City+GA', 'PO Box 8601+City+MI'] },
    { 'General Cable Corporation':  ['PO Box 6575+City+CO', 'PO Box 3855+City+WA', 'PO Box 5401+City+VT'] },
    { 'General Dynamics Corporation':  ['PO Box 2219+City+VT', 'PO Box 418+City+KY', 'PO Box 479+City+FL'] },
    { 'General Electric Company':  ['PO Box 8649+City+TX', 'PO Box 9049+City+MI', 'PO Box 7727+City+GA'] },
    { 'General Mills Inc':  ['PO Box 2363+City+VT', 'PO Box 8090+City+MI', 'PO Box 4373+City+MO'] },
    { 'General Motors Corporation':  ['PO Box 3127+City+TX', 'PO Box 8654+City+MO', 'PO Box 6523+City+FL'] },
    { 'Genesis Health Ventures Inc':  ['PO Box 1561+City+MI', 'PO Box 346+City+WA', 'PO Box 3318+City+WA'] },
    { 'Gentek Inc':  ['PO Box 5763+City+GA', 'PO Box 9384+City+GA', 'PO Box 7088+City+KY'] },
    { 'Gentiva Health Services Inc':  ['PO Box 4973+City+WA', 'PO Box 289+City+CA', 'PO Box 6295+City+CA'] },
    { 'Genuine Parts Company':  ['PO Box 3795+City+FL', 'PO Box 5737+City+GA', 'PO Box 2753+City+MI'] },
    { 'Genuity Inc':  ['PO Box 3318+City+CO', 'PO Box 3361+City+MO', 'PO Box 1288+City+MI'] },
    { 'Genzyme Corporation':  ['PO Box 5860+City+CT', 'PO Box 7912+City+VT', 'PO Box 210+City+MI'] },
    { 'Georgia Gulf Corporation':  ['PO Box 6490+City+FL', 'PO Box 2478+City+CO', 'PO Box 1994+City+FL'] },
    { 'Georgia-Pacific Corporation':  ['PO Box 8285+City+MI', 'PO Box 8681+City+NY', 'PO Box 6160+City+CA'] },
    { 'Gillette Company':  ['PO Box 3394+City+KY', 'PO Box 1978+City+FL', 'PO Box 5983+City+CA'] },
    { 'Gold Kist Inc':  ['PO Box 503+City+CT', 'PO Box 2591+City+WA', 'PO Box 9414+City+MO'] },
    { 'Golden State Bancorp Inc':  ['PO Box 4281+City+FL',' PO Box 26+City+CA', 'PO Box 9968+City+VT'] },
    { 'Golden West Financial Corporation':  ['PO Box 9456+City+NY', 'PO Box 4057+City+NY', 'PO Box 1095+City+MO'] },
    { 'Goldman Sachs Group Inc':  ['PO Box 9199+City+CO', 'PO Box 8531+City+WA', 'PO Box 602+City+CT'] },
    { 'Goodrich Corporation':  ['PO Box 7569+City+KY', 'PO Box 2816+City+MO', 'PO Box 7639+City+CA'] },
    { 'The Goodyear Tire & Rubber Company':  ['PO Box 4134+City+GA', 'PO Box 2157+City+KY', 'PO Box 8578+City+WA'] },
    { 'Granite Construction Incorporated':  ['PO Box 8064+City+VT', 'PO Box 6418+City+GA', 'PO Box 7575+City+FL'] },
    { 'Graybar Electric Company Inc':  ['PO Box 1034+City+TX', 'PO Box 7448+City+VT', 'PO Box 3631+City+GA'] },
    { 'Great Lakes Chemical Corporation':  ['PO Box 9787+City+KY', 'PO Box 5312+City+WA', 'PO Box 187+City+MO'] },
    { 'Great Plains Energy Inc':  ['PO Box 2710+City+MI', 'PO Box 7096+City+WA', 'PO Box 7389+City+CO'] },
    { 'GreenPoint Financial Corp':  ['PO Box 9976+City+CT', 'PO Box 1808+City+GA', 'PO Box 7211+City+GA'] },
    { 'Greif Bros Corporation':  ['PO Box 7025+City+WA', 'PO Box 382+City+CT', 'PO Box 916+City+VT'] },
    { 'Grey Global Group Inc':  ['PO Box 5398+City+CO', 'PO Box 5759+City+CT', 'PO Box 9834+City+KY'] },
    { 'Group 1 Automotive Inc':  ['PO Box 2921+City+MI', 'PO Box 7740+City+CO', 'PO Box 218+City+KY'] },
    { 'Guidant Corporation':  ['PO Box 9496+City+CO', 'PO Box 8556+City+CA', 'PO Box 2566+City+TX'] },
    { 'H&R Block Inc':  ['PO Box 2483+City+GA', 'PO Box 1550+City+KY', 'PO Box 128+City+FL'] },
    { 'HB Fuller Company':  ['PO Box 664+City+NY', 'PO Box 2282+City+GA', 'PO Box 6649+City+KY'] },
    { 'HJ Heinz Company':  ['PO Box 8170+City+GA',' PO Box 5012+City+CO', 'PO Box 7455+City+NY'] },
    { 'Halliburton Co':  ['PO Box 8309+City+TX', 'PO Box 3841+City+KY', 'PO Box 1478+City+CO'] },
    { 'Harley-Davidson Inc':  ['PO Box 4523+City+KY', 'PO Box 3081+City+WA', 'PO Box 591+City+CA'] },
    { 'Harman International Industries Inc':  ['PO Box 2031+City+KY', 'PO Box 4430+City+TX', 'PO Box 432+City+CO'] },
    { 'Harrahs Entertainment Inc':  ['PO Box 16+City+CO', 'PO Box 1345+City+TX PO', 'Box 5710+City+WA'] },
    { 'Harris Corp':  ['PO Box 9983+City+TX', 'PO Box 3892+City+FL', 'PO Box 9078+City+KY'] },
    { 'Harsco Corp':  ['PO Box 5136+City+NY', 'PO Box 4243+City+TX', 'PO Box 3871+City+CA'] },
    { 'Hartford Financial Services Group Inc':  ['PO Box 4159+City+TX', 'PO Box 8646+City+FL', 'PO Box 2965+City+CT'] },
    { 'Hasbro Inc':  ['PO Box 8379+City+VT', 'PO Box 6508+City+WA', 'PO Box 6898+City+VT'] },
    { 'Hawaiian Electric Industries Inc':  ['PO Box 8028+City+TX', 'PO Box 8819+City+MO', 'PO Box 5939+City+CO'] },
    { 'HCA Inc':  ['PO Box 8669+City+CA', 'PO Box 280+City+FL', 'PO Box 2847+City+MI'] },
    { 'Health Management Associates Inc':  ['PO Box 6361+City+TX', 'PO Box 6190+City+VT', 'PO Box 9690+City+FL'] },
    { 'Health Net Inc':  ['PO Box 8991+City+NY', 'PO Box 7314+City+CT', 'PO Box 7837+City+CT'] },
    { 'Healthsouth Corp':  ['PO Box 8053+City+MO', 'PO Box 6772+City+VT', 'PO Box 3944+City+WA'] },
    { 'Henry Schein Inc':  ['PO Box 6064+City+FL', 'PO Box 7882+City+FL', 'PO Box 7572+City+VT'] },
    { 'Hercules Inc':  ['PO Box 5117+City+FL', 'PO Box 2147+City+CA', 'PO Box 4607+City+FL'] },
    { 'Herman Miller Inc':  ['PO Box 8239+City+WA', 'PO Box 3098+City+KY', 'PO Box 3395+City+WA'] },
    { 'Hershey Foods Corp':  ['PO Box 3198+City+KY', 'PO Box 5081+City+KY', 'PO Box 3484+City+TX'] },
    { 'Hewlett-Packard Company':  ['PO Box 6320+City+MO', 'PO Box 7315+City+WA', 'PO Box 2397+City+CT'] },
    { 'Hibernia Corp':  ['PO Box 3293+City+CT', 'PO Box 921+City+VT', 'PO Box 2900+City+NY'] },
    { 'Hillenbrand Industries Inc':  ['PO Box 6317+City+NY', 'PO Box 634+City+MI', 'PO Box 2693+City+KY'] },
    { 'Hilton Hotels Corp':  ['PO Box 5980+City+KY', 'PO Box 2571+City+WA', 'PO Box 3243+City+MO'] },
    { 'Hollywood Entertainment Corp':  ['PO Box 2400+City+CO', 'PO Box 2446+City+CO', 'PO Box 6812+City+KY'] },
    { 'Home Depot Inc':  ['PO Box 9769+City+MO', 'PO Box 2517+City+MI', 'PO Box 4843+City+VT'] },
    { 'Hon Industries Inc':  ['PO Box 442+City+MI', 'PO Box 3197+City+TX', 'PO Box 7588+City+CA'] },
    { 'Honeywell International Inc':  ['PO Box 1482+City+CT',' PO Box 7915+City+CA', 'PO Box 3956+City+GA'] },
    { 'Hormel Foods Corp':  ['PO Box 8923+City+VT', 'PO Box 5590+City+NY', 'PO Box 4149+City+VT'] },
    { 'Host Marriott Corp':  ['PO Box 6249+City+MO', 'PO Box 9777+City+CO', 'PO Box 9213+City+CT'] },
    { 'Household International Corp':  ['PO Box 3157+City+MI', 'PO Box 8505+City+CT', 'PO Box 6913+City+CT'] },
    { 'Hovnanian Enterprises Inc':  ['PO Box 5636+City+KY', 'PO Box 4671+City+KY', 'PO Box 4090+City+TX'] },
    { 'Hub Group Inc':  ['PO Box 2270+City+CA', 'PO Box 6669+City+CT', 'PO Box 8553+City+NY'] },
    { 'Hubbell Inc':  ['PO Box 4581+City+KY', 'PO Box 8765+City+MO', 'PO Box 675+City+GA'] },
    { 'Hughes Supply Inc':  ['PO Box 9025+City+FL', 'PO Box 3976+City+MI', 'PO Box 5326+City+WA'] },
    { 'Humana Inc':  ['PO Box 6817+City+CT', 'PO Box 245+City+VT', 'PO Box 6144+City+NY'] },
    { 'Huntington Bancshares Inc':  ['PO Box 6083+City+CA', 'PO Box 2508+City+MO', 'PO Box 67+City+CO'] },
    { 'Idacorp Inc':  ['PO Box 1708+City+GA', 'PO Box 3024+City+CA', 'PO Box 3072+City+CT'] },
    { 'IDT Corporation':  ['PO Box 4452+City+CA', 'PO Box 3028+City+KY', 'PO Box 5108+City+TX'] },
    { 'IKON Office Solutions Inc':  ['PO Box 2533+City+CT', 'PO Box 316+City+VT', 'PO Box 2775+City+TX'] },
    { 'Illinois Tool Works Inc':  ['PO Box 4307+City+MO', 'PO Box 2536+City+CT', 'PO Box 1255+City+MO'] },
    { 'IMC Global Inc':  ['PO Box 9898+City+TX', 'PO Box 8931+City+WA', 'PO Box 4041+City+CO'] },
    { 'Imperial Sugar Company':  ['PO Box 4165+City+MO', 'PO Box 7135+City+NY', 'PO Box 4464+City+KY'] },
    { 'IMS Health Inc':  ['PO Box 3638+City+CA', 'PO Box 8273+City+KY', 'PO Box 3227+City+FL'] },
    { 'Ingles Market Inc':  ['PO Box 6857+City+KY', 'PO Box 7154+City+GA', 'PO Box 5007+City+VT'] },
    { 'Ingram Micro Inc':  ['PO Box 7524+City+NY', 'PO Box 7415+City+TX', 'PO Box 5258+City+WA'] },
    { 'Insight Enterprises Inc':  ['PO Box 7874+City+CO', 'PO Box 9218+City+GA', 'PO Box 6107+City+NY'] },
    { 'Integrated Electrical Services Inc':  ['PO Box 3785+City+TX', 'PO Box 9480+City+MO', 'PO Box 8378+City+CA'] },
    { 'Intel Corporation':  ['PO Box 9206+City+WA', 'PO Box 4338+City+TX', 'PO Box 2578+City+VT'] },
    { 'International Paper Co':  ['PO Box 6069+City+WA', 'PO Box 8251+City+TX', 'PO Box 2974+City+VT'] },
    { 'Interpublic Group of Companies Inc':  ['PO Box 1172+City+CA', 'PO Box 4847+City+FL', 'PO Box 848+City+CT'] },
    { 'Interstate Bakeries Corporation':  ['PO Box 3008+City+CO', 'PO Box 5681+City+GA', 'PO Box 8210+City+MI'] },
    { 'International Business Machines Corp':  ['PO Box 8618+City+MI', 'PO Box 161+City+GA', 'PO Box 706+City+CO'] },
    { 'International Flavors & Fragrances Inc':  ['PO Box 8774+City+MI', 'PO Box 981+City+KY', 'PO Box 8691+City+MI'] },
    { 'International Multifoods Corporation':  ['PO Box 5056+City+FL', 'PO Box 9739+City+FL', 'PO Box 5492+City+MO'] },
    { 'Intuit Inc':  ['PO Box 4368+City+MO', 'PO Box 859+City+CA', 'PO Box 8536+City+KY'] },
    { 'IT Group Inc':  ['PO Box 2474+City+TX', 'PO Box 8302+City+TX', 'PO Box 9971+City+WA'] },
    { 'ITT Industries Inc':  ['PO Box 4289+City+GA', 'PO Box 7235+City+GA', 'PO Box 1372+City+KY'] },
    { 'Ivax Corp':  ['PO Box 5280+City+VT', 'PO Box 4668+City+VT', 'PO Box 4940+City+MI'] },
    { 'JB Hunt Transport Services Inc':  ['PO Box 4931+City+GA', 'PO Box 3232+City+TX', 'PO Box 5532+City+WA'] },
    { 'JC Penny Co':  ['PO Box 1694+City+GA', 'PO Box 5780+City+CT', 'PO Box 8162+City+MO'] },
    { 'JP Morgan Chase & Co':  ['PO Box 4159+City+GA', 'PO Box 298+City+MI', 'PO Box 6301+City+KY'] },
    { 'Jabil Circuit Inc':  ['PO Box 7747+City+MI', 'PO Box 7081+City+MO', 'PO Box 3701+City+GA'] },
    { 'Jack In The Box Inc':  ['PO Box 1526+City+CT', 'PO Box 705+City+CT', 'PO Box 3546+City+VT'] },
    { 'Jacobs Engineering Group Inc':  ['PO Box 3053+City+CT', 'PO Box 8985+City+CO', 'PO Box 2214+City+MO'] },
    { 'JDS Uniphase Corp':  ['PO Box 227+City+CT', 'PO Box 3573+City+NY', 'PO Box 6013+City+MO'] },
    { 'Jefferson-Pilot Co':  ['PO Box 3053+City+WA',' PO Box 8030+City+FL', 'PO Box 2050+City+MO'] },
    { 'John Hancock Financial Services Inc':  ['PO Box 5873+City+WA', 'PO Box 3907+City+MO', 'PO Box 8113+City+KY'] },
    { 'Johnson & Johnson':  ['PO Box 3140+City+MI', 'PO Box 8173+City+MO', 'PO Box 3831+City+GA'] },
    { 'Johnson Controls Inc':  ['PO Box 9662+City+FL', 'PO Box 1306+City+TX', 'PO Box 3878+City+CT'] },
    { 'Jones Apparel Group Inc':  ['PO Box 2109+City+MI', 'PO Box 9358+City+VT', 'PO Box 3482+City+CA'] },
    { 'KB Home':  ['PO Box 2022+City+MI', 'PO Box 4456+City+KY', 'PO Box 4612+City+MO'] },
    { 'Kellogg Company':  ['PO Box 273+City+TX', 'PO Box 953+City+FL', 'PO Box 2587+City+TX'] },
    { 'Kellwood Company':  ['PO Box 8909+City+GA',' PO Box 6745+City+CT', 'PO Box 4107+City+WA'] },
    { 'Kelly Services Inc':  ['PO Box 2737+City+WA', 'PO Box 9166+City+KY', 'PO Box 6806+City+MI'] },
    { 'Kemet Corp':  ['PO Box 2238+City+NY', 'PO Box 716+City+CT', 'PO Box 2994+City+CT'] },
    { 'Kennametal Inc':  ['PO Box 2050+City+WA', 'PO Box 9713+City+KY', 'PO Box 641+City+MO'] },
    { 'Kerr-McGee Corporation':  ['PO Box 1426+City+GA', 'PO Box 4191+City+WA', 'PO Box 555+City+VT'] },
    { 'KeyCorp':  ['PO Box 9182+City+CO', 'PO Box 8287+City+KY', 'PO Box 6525+City+CA'] },
    { 'KeySpan Corp':  ['PO Box 7867+City+FL', 'PO Box 2156+City+NY', 'PO Box 4067+City+NY'] },
    { 'Kimball International Inc':  ['PO Box 8193+City+CT', 'PO Box 3787+City+CT', 'PO Box 4960+City+NY'] },
    { 'Kimberly-Clark Corporation':  ['PO Box 6305+City+MO', 'PO Box 371+City+MO', 'PO Box 2274+City+TX'] },
    { 'Kindred Healthcare Inc':  ['PO Box 2529+City+TX', 'PO Box 8195+City+TX', 'PO Box 3385+City+NY'] },
    { 'KLA-Tencor Corporation':  ['PO Box 7148+City+CT', 'PO Box 1204+City+FL', 'PO Box 3236+City+TX'] },
    { 'K-Mart Corp':  ['PO Box 2663+City+KY', 'PO Box 3958+City+TX', 'PO Box 3897+City+CO'] },
    { 'Knight-Ridder Inc':  ['PO Box 6281+City+TX', 'PO Box 2384+City+TX', 'PO Box 9204+City+TX'] },
    { 'Kohls Corp':  ['PO Box 7368+City+MI', 'PO Box 8911+City+CT', 'PO Box 3793+City+CO'] },
    { 'KPMG Consulting Inc':  ['PO Box 3648+City+MI', 'PO Box 4442+City+KY', 'PO Box 997+City+CT'] },
    { 'Kroger Co':  ['PO Box 3933+City+GA', 'PO Box 6594+City+FL', 'PO Box 742+City+MO'] },
    { 'L-3 Communications Holdings Inc':  ['PO Box 4805+City+MI', 'PO Box 9047+City+MI', 'PO Box 8208+City+VT'] },
    { 'Laboratory Corporation of America Holdings':  ['PO Box 4687+City+NY', 'PO Box 9117+City+CT', 'PO Box 242+City+VT'] },
    { 'Lam Research Corporation':  ['PO Box 2570+City+CA', 'PO Box 6998+City+CT', 'PO Box 7733+City+FL'] },
    { 'LandAmerica Financial Group Inc':  ['PO Box 8108+City+VT', 'PO Box 3669+City+KY', 'PO Box 938+City+CA'] },
    { 'Lands End Inc':  ['PO Box 3193+City+FL', 'PO Box 3758+City+NY', 'PO Box 257+City+MO'] },
    { 'Landstar System Inc':  ['PO Box 9480+City+CO', 'PO Box 627+City+MI', 'PO Box 5466+City+CT'] },
    { 'La-Z-Boy Inc':  ['PO Box 775+City+TX', 'PO Box 6622+City+FL', 'PO Box 7955+City+CA'] },
    { 'Lear Corporation':  ['PO Box 103+City+GA', 'PO Box 6083+City+MO', 'PO Box 5719+City+CO'] },
    { 'Legg Mason Inc':  ['PO Box 4212+City+CT',' PO Box 4789+City+TX', 'PO Box 2675+City+MO'] },
    { 'Leggett & Platt Inc':  ['PO Box 4688+City+MI', 'PO Box 221+City+TX', 'PO Box 1148+City+KY'] },
    { 'Lehman Brothers Holdings Inc':  ['PO Box 9770+City+TX', 'PO Box 5696+City+CO', 'PO Box 112+City+CA'] },
    { 'Lennar Corporation':  ['PO Box 6924+City+KY', 'PO Box 5750+City+NY', 'PO Box 6695+City+MO'] },
    { 'Lennox International Inc':  ['PO Box 8950+City+CA', 'PO Box 3114+City+FL', 'PO Box 3652+City+TX'] },
    { 'Level 3 Communications Inc':  ['PO Box 1932+City+MI', 'PO Box 9353+City+FL', 'PO Box 8902+City+CO'] },
    { 'Levi Strauss & Co':  ['PO Box 7528+City+TX', 'PO Box 7731+City+CT', 'PO Box 989+City+MO'] },
    { 'Lexmark International Inc':  ['PO Box 4119+City+WA', 'PO Box 6396+City+WA', 'PO Box 6089+City+CO'] },
    { 'Limited Inc':  ['PO Box 7789+City+WA', 'PO Box 2176+City+CA', 'PO Box 9875+City+GA'] },
    { 'Lincoln National Corporation':  ['PO Box 5628+City+WA', 'PO Box 9285+City+KY', 'PO Box 8103+City+WA'] },
    { 'Linens n Things Inc':  ['PO Box 8470+City+KY', 'PO Box 2719+City+VT', 'PO Box 8847+City+WA'] },
    { 'Lithia Motors Inc':  ['PO Box 9274+City+FL', 'PO Box 99+City+CO', 'PO Box 9098+City+VT'] },
    { 'Liz Claiborne Inc':  ['PO Box 5384+City+GA', 'PO Box 3090+City+TX', 'PO Box 4027+City+NY'] },
    { 'Lockheed Martin Corporation':  ['PO Box 3604+City+GA', 'PO Box 9626+City+WA', 'PO Box 4077+City+CO'] },
    { 'Loews Corporation':  ['PO Box 9553+City+GA', 'PO Box 1383+City+FL', 'PO Box 3699+City+NY'] },
    { 'Longs Drug Stores Corporation':  ['PO Box 9130+City+MI', 'PO Box 6752+City+NY', 'PO Box 3558+City+FL'] },
    { 'Louisiana-Pacific Corporation':  ['PO Box 4059+City+NY', 'PO Box 7313+City+TX', 'PO Box 9766+City+VT'] },
    { 'Lowes Companies Inc':  ['PO Box 1714+City+KY', 'PO Box 7762+City+CO', 'PO Box 3476+City+CT'] },
    { 'LSI Logic Corporation':  ['PO Box 1843+City+CT', 'PO Box 4048+City+KY', 'PO Box 7393+City+CO'] },
    { 'The LTV Corporation':  ['PO Box 1055+City+FL', 'PO Box 2149+City+MO', 'PO Box 4539+City+MO'] },
    { 'The Lubrizol Corporation':  ['PO Box 8137+City+MO', 'PO Box 3710+City+KY', 'PO Box 4706+City+TX'] },
    { 'Lucent Technologies Inc':  ['PO Box 2560+City+WA', 'PO Box 6167+City+GA', 'PO Box 5769+City+TX'] },
    { 'Lyondell Chemical Company':  ['PO Box 8843+City+MI', 'PO Box 5673+City+CA', 'PO Box 1417+City+FL'] },
    { 'M & T Bank Corporation':  ['PO Box 2328+City+WA', 'PO Box 5502+City+VT', 'PO Box 3978+City+MO'] },
    { 'Magellan Health Services Inc':  ['PO Box 7288+City+NY', 'PO Box 2091+City+GA', 'PO Box 8680+City+MO'] },
    { 'Mail-Well Inc':  ['PO Box 9973+City+CT', 'PO Box 3420+City+CT', 'PO Box 6035+City+VT'] },
    { 'Mandalay Resort Group':  ['PO Box 2657+City+CT', 'PO Box 8899+City+GA', 'PO Box 9612+City+NY'] },
    { 'Manor Care Inc':  ['PO Box 73+City+MI', 'PO Box 6101+City+KY PO', 'Box 5475+City+CA'] },
    { 'Manpower Inc':  ['PO Box 4200+City+TX', 'PO Box 1271+City+KY', 'PO Box 3287+City+MO'] },
    { 'Marathon Oil Corporation':  ['PO Box 7209+City+GA', 'PO Box 6144+City+CO', 'PO Box 1756+City+TX'] },
    { 'Mariner Health Care Inc':  ['PO Box 2454+City+TX', 'PO Box 7947+City+TX', 'PO Box 201+City+WA'] },
    { 'Markel Corporation':  ['PO Box 6662+City+GA', 'PO Box 159+City+NY', 'PO Box 4480+City+CT'] },
    { 'Marriott International Inc':  ['PO Box 5219+City+MI', 'PO Box 5101+City+FL', 'PO Box 6055+City+TX'] },
    { 'Marsh & McLennan Companies Inc':  ['PO Box 2653+City+MO', 'PO Box 3298+City+CO', 'PO Box 9149+City+GA'] },
    { 'Marsh Supermarkets Inc':  ['PO Box 9097+City+NY', 'PO Box 708+City+FL', 'PO Box 4866+City+MI'] },
    { 'Marshall & Ilsley Corporation':  ['PO Box 7045+City+WA', 'PO Box 8863+City+VT', 'PO Box 5427+City+WA'] },
    { 'Martin Marietta Materials Inc':  ['PO Box 4670+City+NY', 'PO Box 5803+City+GA', 'PO Box 4387+City+TX'] },
    { 'Masco Corporation':  ['PO Box 3739+City+GA', 'PO Box 9555+City+FL', 'PO Box 4045+City+VT'] },
    { 'Massey Energy Company':  ['PO Box 3244+City+VT', 'PO Box 1907+City+CO', 'PO Box 3238+City+CT'] },
    { 'MasTec Inc':  ['PO Box 5528+City+TX', 'PO Box 4021+City+MI', 'PO Box 9281+City+NY'] },
    { 'Mattel Inc':  ['PO Box 8031+City+GA', 'PO Box 2909+City+MI', 'PO Box 5455+City+TX'] },
    { 'Maxim Integrated Products Inc':  ['PO Box 5911+City+GA', 'PO Box 6346+City+CT', 'PO Box 4017+City+TX'] },
    { 'Maxtor Corporation':  ['PO Box 283+City+CO', 'PO Box 7645+City+TX', 'PO Box 3486+City+NY'] },
    { 'Maxxam Inc':  ['PO Box 32+City+FL', 'PO Box 1004+City+CO', 'PO Box 6735+City+CO'] },
    { 'The May Department Stores Company':  ['PO Box 1821+City+GA', 'PO Box 3767+City+MI', 'PO Box 1947+City+MO'] },
    { 'Maytag Corporation':  ['PO Box 5982+City+FL', 'PO Box 3911+City+KY', 'PO Box 6180+City+VT'] },
    { 'MBNA Corporation':  ['PO Box 2458+City+WA', 'PO Box 7264+City+MO', 'PO Box 5491+City+MO'] },
    { 'McCormick & Company Incorporated':  ['PO Box 7170+City+KY', 'PO Box 7641+City+VT', 'PO Box 7037+City+MO'] },
    { 'McDonalds Corporation':  ['PO Box 7892+City+CA', 'PO Box 9092+City+CA', 'PO Box 2230+City+KY'] },
    { 'The McGraw-Hill Companies Inc':  ['PO Box 2586+City+CT', 'PO Box 8865+City+CT', 'PO Box 7799+City+WA'] },
    { 'McKesson Corporation':  ['PO Box 8993+City+GA', 'PO Box 1842+City+TX', 'PO Box 7886+City+MI'] },
    { 'McLeodUSA Incorporated':  ['PO Box 870+City+WA', 'PO Box 2428+City+FL', 'PO Box 2399+City+GA'] },
    { 'MDC Holdings Inc':  ['PO Box 3989+City+GA',' PO Box 6532+City+MI', 'PO Box 6185+City+NY'] },
    { 'MDU Resources Group Inc':  ['PO Box 9416+City+WA', 'PO Box 131+City+GA', 'PO Box 3928+City+MO'] },
    { 'MeadWestvaco Corporation':  ['PO Box 4666+City+FL', 'PO Box 6560+City+CA', 'PO Box 6437+City+NY'] },
    { 'Medtronic Inc':  ['PO Box 5066+City+GA', 'PO Box 5813+City+WA', 'PO Box 4361+City+CT'] },
    { 'Mellon Financial Corporation':  ['PO Box 2296+City+TX', 'PO Box 9869+City+GA', 'PO Box 1470+City+WA'] },
    { 'The Mens Wearhouse Inc':  ['PO Box 8109+City+NY', 'PO Box 5681+City+NY', 'PO Box 8477+City+KY'] },
    { 'Merck & Co Inc':  ['PO Box 3804+City+MI', 'PO Box 4440+City+CO', 'PO Box 9594+City+CO'] },
    { 'Mercury General Corporation':  ['PO Box 5992+City+MO', 'PO Box 9772+City+FL', 'PO Box 9868+City+FL'] },
    { 'Merrill Lynch & Co Inc':  ['PO Box 1677+City+CO', 'PO Box 6237+City+TX', 'PO Box 1879+City+NY'] },
    { 'Metaldyne Corporation':  ['PO Box 5500+City+GA', 'PO Box 3401+City+CO', 'PO Box 9525+City+WA'] },
    { 'Metals USA Inc':  ['PO Box 238+City+FL', 'PO Box 5435+City+CO', 'PO Box 954+City+WA'] },
    { 'MetLife Inc':  ['PO Box 9081+City+GA',' PO Box 8911+City+CO', 'PO Box 6462+City+CT'] },
    { 'Metris Companies Inc':  ['PO Box 9806+City+MI', 'PO Box 2775+City+MI', 'PO Box 1710+City+TX'] },
    { 'MGIC Investment Corporation':  ['PO Box 2620+City+GA', 'PO Box 5409+City+MI', 'PO Box 4941+City+MO'] },
    { 'MGM Mirage':  ['PO Box 4496+City+GA', 'PO Box 5499+City+KY', 'PO Box 4680+City+MI'] },
    { 'Michaels Stores Inc':  ['PO Box 3261+City+NY', 'PO Box 4363+City+NY', 'PO Box 5316+City+WA'] },
    { 'Micron Technology Inc':  ['PO Box 6440+City+NY', 'PO Box 1631+City+WA', 'PO Box 5840+City+CT'] },
    { 'Microsoft Corporation':  ['PO Box 8662+City+FL', 'PO Box 6165+City+WA', 'PO Box 4874+City+TX'] },
    { 'Milacron Inc':  ['PO Box 3881+City+WA', 'PO Box 4173+City+FL', 'PO Box 6328+City+GA'] },
    { 'Millennium Chemicals Inc':  ['PO Box 9367+City+VT', 'PO Box 1456+City+KY', 'PO Box 6865+City+CT'] },
    { 'Mirant Corporation':  ['PO Box 6895+City+MO', 'PO Box 8875+City+CT', 'PO Box 3667+City+WA'] },
    { 'Mohawk Industries Inc':  ['PO Box 2351+City+NY', 'PO Box 8735+City+TX', 'PO Box 6683+City+MI'] },
    { 'Molex Incorporated':  ['PO Box 1188+City+CO', 'PO Box 5249+City+CA', 'PO Box 509+City+NY'] },
    { 'The MONY Group Inc':  ['PO Box 7667+City+CO', 'PO Box 8477+City+MI', 'PO Box 3651+City+GA'] },
    { 'Morgan Stanley Dean Witter & Co':  ['PO Box 2521+City+CT', 'PO Box 4004+City+VT', 'PO Box 9432+City+MO'] },
    { 'Motorola Inc':  ['PO Box 6907+City+CA', 'PO Box 9657+City+NY', 'PO Box 7106+City+WA'] },
    { 'MPS Group Inc':  ['PO Box 7907+City+GA', 'PO Box 8185+City+WA', 'PO Box 5841+City+CO'] },
    { 'Murphy Oil Corporation':  ['PO Box 7204+City+FL', 'PO Box 2446+City+WA', 'PO Box 840+City+VT'] },
    { 'Nabors Industries Inc':  ['PO Box 3733+City+CA', 'PO Box 7429+City+KY', 'PO Box 9356+City+NY'] },
    { 'Nacco Industries Inc':  ['PO Box 6316+City+GA', 'PO Box 518+City+VT', 'PO Box 1524+City+KY'] },
    { 'Nash Finch Company':  ['PO Box 5566+City+KY', 'PO Box 4859+City+CA', 'PO Box 176+City+TX'] },
    { 'National City Corp':  ['PO Box 1476+City+VT', 'PO Box 7307+City+FL', 'PO Box 9832+City+FL'] },
    { 'National Commerce Financial Corporation':  ['PO Box 6675+City+MI', 'PO Box 2489+City+VT', 'PO Box 8686+City+TX'] },
    { 'National Fuel Gas Company':  ['PO Box 4738+City+FL', 'PO Box 3685+City+WA', 'PO Box 2139+City+TX'] }
]


def get_payment_list():
    num_payments_to_do = 10000
    for _ in range(num_payments_to_do):
        payment_list.append(generate_random_payment())
    return payment_list


def generate_random_payment():
    # Randomly generate an index roughly following a normal distribution 
    squared_index = random.randrange(len(company_list)) ** 2
    company_index = math.floor(math.sqrt(squared_index))

    # Get business and its info
    business = company_list[company_index]
    company_name = list(business.keys())[0]
    company_name = typo_the_name(company_name)
    address_list = list(business.values())[0]
    address = address_list[random.randrange(len(address_list))]
    amount = str(random.randrange(2000))
    return [company_name, address, amount]


def typo_the_name(name):
    rand_num = random.randrange(10)
    if rand_num >= 3:
        return name
    else:
        # Replace 'o' with a random lowercase letter
        return name.replace('o', chr(random.randrange(97,122)))


if __name__ == '__main__':
    payments = get_payment_list()
    with open('./payments.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for row in payments:
            writer.writerow(row)