import time
import random
from typing import Union
from ..rustplus_proto import AppEntityPayload


class EntityManager:

    def __init__(self) -> None:
        self.entities = {}
        self.ids = [-2139580305, -2124352573, -2123125470, -2107018088, -2103694546, -2099697608, -2097376851, -2094954543,
               -2086926071, -2084071424, -2072273936, -2069578888, -2067472972, -2058362263, -2049214035, -2047081330,
               -2040817543, -2025184684, -2022172587, -2012470695, -2002277461, -2001260025, -1999722522, -1997698639,
               -1997543660, -1994909036, -1992717673, -1985799200, -1982036270, -1978999529, -1973785141, -1966748496,
               -1962971928, -1961560162, -1958316066, -1950721390, -1941646328, -1938052175, -1916473915, -1904821376,
               -1903165497, -1899491405, -1884328185, -1880870149, -1880231361, -1878764039, -1878475007, -1863559151,
               -1861522751, -1850571427, -1848736516, -1841918730, -1832422579, -1824943010, -1819763926, -1819233322,
               -1815301988, -1812555177, -1802083073, -1800345240, -1785231475, -1780802565, -1779183908, -1779180711,
               -1778897469, -1778159885, -1776128552, -1773144852, -1772746857, -1768880890, -1759188988, -1758372725,
               -1754948969, -1736356576, -1729415579, -1709878924, -1698937385, -1695367501, -1693832478, -1691396643,
               -1685290200, -1679267738, -1677315902, -1673693549, -1671551935, -1667224349, -1663759755, -1654233406,
               -1651220691, -1647846966, -1622660759, -1622110948, -1621539785, -1615281216, -1614955425, -1607980696,
               -1588628467, -1583967946, -1581843485, -1579932985, -1569700847, -1557377697, -1553999294, -1549739227,
               -1539025626, -1538109120, -1535621066, -1530414568, -1520560807, -1519126340, -1518883088, -1517740219,
               -1511285251, -1509851560, -1507239837, -1506417026, -1506397857, -1501451746, -1488398114, -1486461488,
               -1478445584, -1478212975, -1478094705, -1469578201, -1448252298, -1442559428, -1440987069, -1432674913,
               -1429456799, -1423304443, -1408336705, -1405508498, -1379835144, -1379036069, -1370759135, -1368584029,
               -1367281941, -1336109173, -1331212963, -1330640246, -1321651331, -1316706473, -1306288356, -1305326964,
               -1302129395, -1293296287, -1286302544, -1284169891, -1273339005, -1266045928, -1262185308, -1252059217,
               -1234735557, -1215753368, -1215166612, -1211268013, -1211166256, -1199897172, -1199897169, -1184406448,
               -1183726687, -1167031859, -1166712463, -1163532624, -1162759543, -1157596551, -1138208076, -1137865085,
               -1130709577, -1130350864, -1123473824, -1117626326, -1113501606, -1112793865, -1108136649, -1104881824,
               -1102429027, -1101924344, -1100422738, -1100168350, -1078639462, -1073015016, -1049881973, -1044468317,
               -1043618880, -1039528932, -1036635990, -1023374709, -1023065463, -1022661119, -1021495308, -1018587433,
               -1009359066, -1004426654, -1002156085, -1000573653, -996920608, -996185386, -992286106, -989755543,
               -985781766, -979951147, -979302481, -967648160, -961457160, -956706906, -946369541, -939424778,
               -932201673, -930193596, -929092070, -924959988, -912398867, -904863145, -888153050, -886280491,
               -858312878, -855748505, -854270928, -852563019, -851988960, -850982208, -845557339, -819720157,
               -810326667, -804769727, -803263829, -798293154, -796583652, -784870360, -781014061, -778875547,
               -778367295, -769647921, -765183617, -761829530, -751151717, -746647361, -746030907, -742865266,
               -733625651, -727717969, -722241321, -702051347, -700591459, -699558439, -697981032, -695978112,
               -695124222, -692338819, -691113464, -690968985, -690276911, -682687162, -656349006, -649128577,
               -629028935, -626174997, -592016202, -587989372, -586784898, -586342290, -583379016, -582782051,
               -575744869, -575483084, -568419968, -567909622, -566907190, -563624462, -560304835, -559599960,
               -557539629, -555122905, -544317637, -542577259, -541206665, -520133715, -515830359, -502177121,
               -496584751, -493159321, -489848205, -487356515, -484206264, -465682601, -463122489, -458565393,
               -454370658, -395377963, -384243979, -369760990, -365097295, -363689972, -343857907, -335089230,
               -333406828, -324675402, -321733511, -321431890, -316250604, -295829489, -282113991, -280223496,
               -277057363, -265876753, -265292885, -262590403, -253079493, -242084766, -239306133, -237809779,
               -216999575, -216116642, -211235948, -209869746, -196667575, -194953424, -194509282, -187031121,
               -180129657, -176608084, -173268132, -173268131, -173268129, -173268126, -173268125, -156748077,
               -151838493, -151387974, -148794216, -148229307, -144417939, -143132326, -135252633, -132516482,
               -132247350, -129230242, -126305173, -119235651, -113413047, -110921842, -99886070, -97956382, -97459906,
               -92759291, -89874794, -78533081, -75944661, -48090175, -44876289, -44066823, -44066790, -44066600,
               -41896755, -41440462, -33009419, -25740268, -23994173, -22883916, -20045316, -17123659, -8312704,
               -7270019, -4031221, 3222790, 3380160, 14241751, 15388698, 20489901, 21402876, 23352662, 23391694,
               28201841, 37122747, 39600618, 42535890, 51984655, 60528587, 62577426, 69511070, 73681876, 95950017,
               98508942, 99588025, 121049755, 122783240, 143803535, 170758448, 171931394, 174866732, 176787552,
               177226991, 185586769, 190184021, 196700171, 198438816, 200773292, 204391461, 204970153, 215754713,
               223891266, 237239288, 254522515, 261913429, 263834859, 268565518, 271048478, 273172220, 273951840,
               277730763, 282103175, 286193827, 286648290, 296519935, 304481038, 317398316, 342438846, 349762871,
               352130972, 352321488, 352499047, 359723196, 363163265, 363467698, 390728933, 418081930, 442289265,
               442886268, 443432036, 476066818, 479143914, 479292118, 492357192, 524678627, 528668503, 553270375,
               553887414, 559147458, 567235583, 567871954, 573676040, 573926264, 576509618, 588596902, 593465182,
               596469572, 602741290, 603811464, 605467368, 609049394, 613961768, 621915341, 634478325, 642482233,
               649912614, 656371026, 656371027, 656371028, 657352755, 665332906, 671063303, 671706427, 674734128,
               680234026, 696029452, 699075597, 722955039, 756517185, 762289806, 785728077, 794356786, 794443127,
               795236088, 795371088, 803222026, 803954639, 809199956, 809942731, 813023040, 818733919, 818877484,
               826309791, 830839496, 832133926, 833533164, 838831151, 844440409, 850280505, 853471967, 854447607,
               858486327, 866332017, 866889860, 878301596, 882559853, 884424049, 888415708, 895374329, 915408809,
               926800282, 935692442, 936496778, 946662961, 952603248, 963906841, 968019378, 968421290, 971362526,
               980333378, 988652725, 989925924, 996293980, 998894949, 999690781, 1015352446, 1052926200, 1055319033,
               1058261682, 1072924620, 1079279582, 1081315464, 1081921512, 1090916276, 1094293920, 1099314009,
               1103488722, 1104520648, 1110385766, 1112162468, 1121925526, 1142993169, 1149964039, 1153652756,
               1158340331, 1158340332, 1158340334, 1159991980, 1160881421, 1171735914, 1177596584, 1181207482,
               1186655046, 1189981699, 1199391518, 1205084994, 1205607945, 1221063409, 1230323789, 1234878710,
               1234880403, 1242482355, 1242522330, 1248356124, 1258768145, 1259919256, 1263920163, 1266491000,
               1272194103, 1272430949, 1272768630, 1293102274, 1305578813, 1315082560, 1318558775, 1319617282,
               1324203999, 1326180354, 1327005675, 1330084809, 1346158228, 1353298668, 1358643074, 1366282552,
               1367190888, 1371909803, 1373240771, 1373971859, 1376065505, 1381010055, 1382263453, 1390353317,
               1391703481, 1397052267, 1400460850, 1401987718, 1409529282, 1413014235, 1414245162, 1414245522,
               1422530437, 1424075905, 1426574435, 1443579727, 1451568081, 1478091698, 1480022580, 1488979457,
               1491189398, 1512054436, 1516985844, 1521286012, 1523195708, 1523403414, 1524187186, 1525520776,
               1533551194, 1534542921, 1536610005, 1540934679, 1542290441, 1545779598, 1548091822, 1553078977,
               1557173737, 1559779253, 1568388703, 1569882109, 1581210395, 1588298435, 1588492232, 1601468620,
               1602646136, 1608640313, 1629293099, 1638322904, 1643667218, 1655650836, 1655979682, 1658229558,
               1659114910, 1659447559, 1660145984, 1668129151, 1668858301, 1675639563, 1686524871, 1696050067,
               1697996440, 1711033574, 1712070256, 1712261904, 1714496074, 1719978075, 1722154847, 1723747470,
               1729120840, 1729374708, 1729712564, 1735402444, 1744298439, 1746956556, 1751045826, 1757265204,
               1770475779, 1770744540, 1771755747, 1776460938, 1783512007, 1784406797, 1789825282, 1796682209,
               1803831286, 1814288539, 1827479659, 1835946060, 1840570710, 1840822026, 1849887541, 1850456855,
               1856217390, 1873897110, 1874610722, 1877339384, 1882709339, 1883981798, 1883981800, 1883981801,
               1885488976, 1895235349, 1898094925, 1899610628, 1903654061, 1905387657, 1911552868, 1917703890,
               1931713481, 1946219319, 1948067030, 1950721418, 1951603367, 1953903201, 1965232394, 1973165031,
               1973684065, 1975934948, 1983621560, 1989785143, 1992974553, 2009734114, 2019042823, 2021351233,
               2023888403, 2024467711, 2040726127, 2041899972, 2048317869, 2052270186, 2063916636, 2070189026,
               2087678962, 2090395347, 2100007442, 2104517339, 2106561762, 2114754781, 2126889441, 2133269020,
               -1843426638, 343045591, ]

    def get_or_create_entity(self, entity_id: int, get: bool, value: bool = None) -> Union[None, AppEntityPayload]:
        if not get:
            if value is not None:
                # Means we are setting and we have a value
                self.entities[entity_id].value = value
        else:
            # Means we are getting
            if entity_id in self.entities:
                # Means the entity has already been created
                entity_data = self.entities[entity_id]
                if entity_data.protectionExpiry <= time.time():
                    entity_data.protectionExpiry = int(time.time() + random.randint(30*60, 60*60*24*5))
                return entity_data
            else:
                # We need to create an AppEntityPayload
                if entity_id % 3 == 2:
                    payload = AppEntityPayload(
                        value=False,
                        capacity=30,
                        hasProtection=True,
                        protectionExpiry=int(time.time() + random.randint(30*60, 60*60*24*5)),
                        items=[
                            AppEntityPayload.Item(
                                itemId=random.choice(self.ids),
                                quantity=random.randint(1, 1000),
                                itemIsBlueprint=bool(random.randint(0, 1)),
                            ) for _ in range(random.randint(0, 7))
                        ],
                    )
                else:
                    payload = AppEntityPayload(
                        value=bool(random.randint(0, 1)),
                        capacity=0,
                        hasProtection=True,
                        protectionExpiry=int(time.time() + random.randint(30*60, 60*60*24*5)),
                        items=[],
                    )

                self.entities[entity_id] = payload
                return payload
