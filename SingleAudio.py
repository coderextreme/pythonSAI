print('<!--')
import x3d
print('-->')
X3D0 = x3d.X3D()
X3D0.profile = "Full"
X3D0.version = "4.0"
head1 = x3d.head()
meta2 = x3d.meta()
meta2.name = "title"
meta2.content = "SingleAudio.x3d"

head1.children.append(meta2)
meta3 = x3d.meta()
meta3.name = "description"
meta3.content = "The first demo contains a concise X3D scene. The scenario here is the implementation of a single sound source, which is represented by a 3D object. The spatiality of the sound is expressed by a process, in which when the user approaching nearby to the sound source the volume is increased and accordingly when removed there from is reduced. In addition to this and depending on the side of the sound source that the user observes, the sound is emitted from the corresponding speaker. Apart from the 3D scene, we have also added an analyser slider. The analyser gives the possibility to receive real-time generated data, without any change from the input to output sound information. Through this process we achieved the audio visualization of the sound source."

head1.children.append(meta3)
meta4 = x3d.meta()
meta4.name = "info"
meta4.content = "This work presents an innovative solution of the spatial sound in X3DOM framework, that based on a combinational methodology. Specifically, we suggested the enrichment of X3DOM with spatial sound features, using both the X3D sound nodes and the structure of Web Audio API."

head1.children.append(meta4)
meta5 = x3d.meta()
meta5.name = "creator"
meta5.content = "Efi Lakka, Athanasios Malamos, Dick Puk, Don Brutzman"

head1.children.append(meta5)
meta6 = x3d.meta()
meta6.name = "created"
meta6.content = "28 October 2020"

head1.children.append(meta6)
meta7 = x3d.meta()
meta7.name = "modified"
meta7.content = "5 December 2021"

head1.children.append(meta7)
meta8 = x3d.meta()
meta8.name = "reference"
meta8.content = "CHANGELOG.txt"

head1.children.append(meta8)
meta9 = x3d.meta()
meta9.name = "TODO"
meta9.content = "where is AudioClip source?"

head1.children.append(meta9)
meta10 = x3d.meta()
meta10.name = "TODO"
meta10.content = "credit for audio files"

head1.children.append(meta10)
meta11 = x3d.meta()
meta11.name = "reference"
meta11.content = "https://medialab.hmu.gr/minipages/x3domAudio"

head1.children.append(meta11)
meta12 = x3d.meta()
meta12.name = "identifier"
meta12.content = "https://x3dgraphics.com/examples/X3dForAdvancedModeling/AudioSpatialSound/SingleAudio.x3d"

head1.children.append(meta12)
meta13 = x3d.meta()
meta13.name = "generator"
meta13.content = "X3D-Edit 4.0, https://savage.nps.edu/X3D-Edit"

head1.children.append(meta13)
meta14 = x3d.meta()
meta14.name = "license"
meta14.content = "../license.html"

head1.children.append(meta14)

X3D0.head = head1
Scene15 = x3d.Scene()
WorldInfo16 = x3d.WorldInfo()
WorldInfo16.title = "SingleAudio.x3d"

Scene15.children.append(WorldInfo16)
NavigationInfo17 = x3d.NavigationInfo()
NavigationInfo17.DEF = "NAV"

Scene15.children.append(NavigationInfo17)
Background18 = x3d.Background()
Background18.backUrl = ["images/generic/BK1.png","https://x3dgraphics.com/examples/X3dForAdvancedModeling/AudioSpatialSound/images/generic/BK1.png"]
Background18.bottomUrl = ["images/generic/DN1.png","https://x3dgraphics.com/examples/X3dForAdvancedModeling/AudioSpatialSound/images/generic/DN1.png"]
Background18.frontUrl = ["images/generic/FR1.png","https://x3dgraphics.com/examples/X3dForAdvancedModeling/AudioSpatialSound/images/generic/FR1.png"]
Background18.leftUrl = ["images/generic/LF1.png","https://x3dgraphics.com/examples/X3dForAdvancedModeling/AudioSpatialSound/images/generic/LF1.png"]
Background18.rightUrl = ["images/generic/RT1.png","https://x3dgraphics.com/examples/X3dForAdvancedModeling/AudioSpatialSound/images/generic/RT1.png"]
Background18.topUrl = ["images/generic/UP1.png","https://x3dgraphics.com/examples/X3dForAdvancedModeling/AudioSpatialSound/images/generic/UP1.png"]

Scene15.children.append(Background18)
Viewpoint19 = x3d.Viewpoint()
Viewpoint19.DEF = "Camera001"
Viewpoint19.description = "Camera001"
Viewpoint19.farDistance = 0
Viewpoint19.nearDistance = 1
Viewpoint19.orientation = [1,0,0,-0.523599]
Viewpoint19.position = [0,2000,3500]

Scene15.children.append(Viewpoint19)
Transform20 = x3d.Transform()
Transform20.DEF = "Floor"
Transform20.translation = [1.241,0,0.358]
Shape21 = x3d.Shape()
Appearance22 = x3d.Appearance()
Appearance22.DEF = "WireColor"
Material23 = x3d.Material()
Material23.diffuseColor = [0.122,0.114,0.125]

Appearance22.material = Material23

Shape21.appearance = Appearance22
IndexedFaceSet24 = x3d.IndexedFaceSet()
IndexedFaceSet24.DEF = "Box001-GEOMETRY"
IndexedFaceSet24.coordIndex = [0,1,2,-1,3,4,5,-1,6,7,8,-1,9,10,11,-1,12,13,14,-1,15,16,17,-1,18,19,20,-1,21,22,23,-1,24,25,26,-1,27,28,29,-1,30,31,32,-1,33,34,35,-1]
IndexedFaceSet24.solid = False
Coordinate25 = x3d.Coordinate()

IndexedFaceSet24.coord = Coordinate25
Normal26 = x3d.Normal()

IndexedFaceSet24.normal = Normal26

Shape21.geometry = IndexedFaceSet24

Transform20.children.append(Shape21)

Scene15.children.append(Transform20)
Transform27 = x3d.Transform()
Transform27.DEF = "TransformAudio1"
Shape28 = x3d.Shape()
Appearance29 = x3d.Appearance()
Appearance29.DEF = "WireColor_1"
Material30 = x3d.Material()
Material30.diffuseColor = [0.690196,0.101961,0.101961]

Appearance29.material = Material30

Shape28.appearance = Appearance29
IndexedFaceSet31 = x3d.IndexedFaceSet()
IndexedFaceSet31.DEF = "Sphere001-GEOMETRY"
IndexedFaceSet31.coordIndex = [0,1,2,-1,3,4,5,-1,6,7,8,-1,9,10,11,-1,12,13,14,-1,15,16,17,-1,18,19,20,-1,21,22,23,-1,24,25,26,-1,27,28,29,-1,30,31,32,-1,33,34,35,-1,36,37,38,-1,39,40,41,-1,42,43,44,-1,45,46,47,-1,48,49,50,-1,51,52,53,-1,54,55,56,-1,57,58,59,-1,60,61,62,-1,63,64,65,-1,66,67,68,-1,69,70,71,-1,72,73,74,-1,75,76,77,-1,78,79,80,-1,81,82,83,-1,84,85,86,-1,87,88,89,-1,90,91,92,-1,93,94,95,-1,96,97,98,-1,99,100,101,-1,102,103,104,-1,105,106,107,-1,108,109,110,-1,111,112,113,-1,114,115,116,-1,117,118,119,-1,120,121,122,-1,123,124,125,-1,126,127,128,-1,129,130,131,-1,132,133,134,-1,135,136,137,-1,138,139,140,-1,141,142,143,-1,144,145,146,-1,147,148,149,-1,150,151,152,-1,153,154,155,-1,156,157,158,-1,159,160,161,-1,162,163,164,-1,165,166,167,-1,168,169,170,-1,171,172,173,-1,174,175,176,-1,177,178,179,-1,180,181,182,-1,183,184,185,-1,186,187,188,-1,189,190,191,-1,192,193,194,-1,195,196,197,-1,198,199,200,-1,201,202,203,-1,204,205,206,-1,207,208,209,-1,210,211,212,-1,213,214,215,-1,216,217,218,-1,219,220,221,-1,222,223,224,-1,225,226,227,-1,228,229,230,-1,231,232,233,-1,234,235,236,-1,237,238,239,-1,240,241,242,-1,243,244,245,-1,246,247,248,-1,249,250,251,-1,252,253,254,-1,255,256,257,-1,258,259,260,-1,261,262,263,-1,264,265,266,-1,267,268,269,-1,270,271,272,-1,273,274,275,-1,276,277,278,-1,279,280,281,-1,282,283,284,-1,285,286,287,-1,288,289,290,-1,291,292,293,-1,294,295,296,-1,297,298,299,-1,300,301,302,-1,303,304,305,-1,306,307,308,-1,309,310,311,-1,312,313,314,-1,315,316,317,-1,318,319,320,-1,321,322,323,-1,324,325,326,-1,327,328,329,-1,330,331,332,-1,333,334,335,-1,336,337,338,-1,339,340,341,-1,342,343,344,-1,345,346,347,-1,348,349,350,-1,351,352,353,-1,354,355,356,-1,357,358,359,-1,360,361,362,-1,363,364,365,-1,366,367,368,-1,369,370,371,-1,372,373,374,-1,375,376,377,-1,378,379,380,-1,381,382,383,-1,384,385,386,-1,387,388,389,-1,390,391,392,-1,393,394,395,-1,396,397,398,-1,399,400,401,-1,402,403,404,-1,405,406,407,-1,408,409,410,-1,411,412,413,-1,414,415,416,-1,417,418,419,-1,420,421,422,-1,423,424,425,-1,426,427,428,-1,429,430,431,-1,432,433,434,-1,435,436,437,-1,438,439,440,-1,441,442,443,-1,444,445,446,-1,447,448,449,-1,450,451,452,-1,453,454,455,-1,456,457,458,-1,459,460,461,-1,462,463,464,-1,465,466,467,-1,468,469,470,-1,471,472,473,-1,474,475,476,-1,477,478,479,-1,480,481,482,-1,483,484,485,-1,486,487,488,-1,489,490,491,-1,492,493,494,-1,495,496,497,-1,498,499,500,-1,501,502,503,-1,504,505,506,-1,507,508,509,-1,510,511,512,-1,513,514,515,-1,516,517,518,-1,519,520,521,-1,522,523,524,-1,525,526,527,-1,528,529,530,-1,531,532,533,-1,534,535,536,-1,537,538,539,-1,540,541,542,-1,543,544,545,-1,546,547,548,-1,549,550,551,-1,552,553,554,-1,555,556,557,-1,558,559,560,-1,561,562,563,-1,564,565,566,-1,567,568,569,-1,570,571,572,-1,573,574,575,-1,576,577,578,-1,579,580,581,-1,582,583,584,-1,585,586,587,-1,588,589,590,-1,591,592,593,-1,594,595,596,-1,597,598,599,-1,600,601,602,-1,603,604,605,-1,606,607,608,-1,609,610,611,-1,612,613,614,-1,615,616,617,-1,618,619,620,-1,621,622,623,-1,624,625,626,-1,627,628,629,-1,630,631,632,-1,633,634,635,-1,636,637,638,-1,639,640,641,-1,642,643,644,-1,645,646,647,-1,648,649,650,-1,651,652,653,-1,654,655,656,-1,657,658,659,-1,660,661,662,-1,663,664,665,-1,666,667,668,-1,669,670,671,-1,672,673,674,-1,675,676,677,-1,678,679,680,-1,681,682,683,-1,684,685,686,-1,687,688,689,-1,690,691,692,-1,693,694,695,-1,696,697,698,-1,699,700,701,-1,702,703,704,-1,705,706,707,-1,708,709,710,-1,711,712,713,-1,714,715,716,-1,717,718,719,-1,720,721,722,-1,723,724,725,-1,726,727,728,-1,729,730,731,-1,732,733,734,-1,735,736,737,-1,738,739,740,-1,741,742,743,-1,744,745,746,-1,747,748,749,-1,750,751,752,-1,753,754,755,-1,756,757,758,-1,759,760,761,-1,762,763,764,-1,765,766,767,-1,768,769,770,-1,771,772,773,-1,774,775,776,-1,777,778,779,-1,780,781,782,-1,783,784,785,-1,786,787,788,-1,789,790,791,-1,792,793,794,-1,795,796,797,-1,798,799,800,-1,801,802,803,-1,804,805,806,-1,807,808,809,-1,810,811,812,-1,813,814,815,-1,816,817,818,-1,819,820,821,-1,822,823,824,-1,825,826,827,-1,828,829,830,-1,831,832,833,-1,834,835,836,-1,837,838,839,-1,840,841,842,-1,843,844,845,-1,846,847,848,-1,849,850,851,-1,852,853,854,-1,855,856,857,-1,858,859,860,-1,861,862,863,-1,864,865,866,-1,867,868,869,-1,870,871,872,-1,873,874,875,-1,876,877,878,-1,879,880,881,-1,882,883,884,-1,885,886,887,-1,888,889,890,-1,891,892,893,-1,894,895,896,-1,897,898,899,-1,900,901,902,-1,903,904,905,-1,906,907,908,-1,909,910,911,-1,912,913,914,-1,915,916,917,-1,918,919,920,-1,921,922,923,-1,924,925,926,-1,927,928,929,-1,930,931,932,-1,933,934,935,-1,936,937,938,-1,939,940,941,-1,942,943,944,-1,945,946,947,-1,948,949,950,-1,951,952,953,-1,954,955,956,-1,957,958,959,-1,960,961,962,-1,963,964,965,-1,966,967,968,-1,969,970,971,-1,972,973,974,-1,975,976,977,-1,978,979,980,-1,981,982,983,-1,984,985,986,-1,987,988,989,-1,990,991,992,-1,993,994,995,-1,996,997,998,-1,999,1000,1001,-1,1002,1003,1004,-1,1005,1006,1007,-1,1008,1009,1010,-1,1011,1012,1013,-1,1014,1015,1016,-1,1017,1018,1019,-1,1020,1021,1022,-1,1023,1024,1025,-1,1026,1027,1028,-1,1029,1030,1031,-1,1032,1033,1034,-1,1035,1036,1037,-1,1038,1039,1040,-1,1041,1042,1043,-1,1044,1045,1046,-1,1047,1048,1049,-1,1050,1051,1052,-1,1053,1054,1055,-1,1056,1057,1058,-1,1059,1060,1061,-1,1062,1063,1064,-1,1065,1066,1067,-1,1068,1069,1070,-1,1071,1072,1073,-1,1074,1075,1076,-1,1077,1078,1079,-1,1080,1081,1082,-1,1083,1084,1085,-1,1086,1087,1088,-1,1089,1090,1091,-1,1092,1093,1094,-1,1095,1096,1097,-1,1098,1099,1100,-1,1101,1102,1103,-1,1104,1105,1106,-1,1107,1108,1109,-1,1110,1111,1112,-1,1113,1114,1115,-1,1116,1117,1118,-1,1119,1120,1121,-1,1122,1123,1124,-1,1125,1126,1127,-1,1128,1129,1130,-1,1131,1132,1133,-1,1134,1135,1136,-1,1137,1138,1139,-1,1140,1141,1142,-1,1143,1144,1145,-1,1146,1147,1148,-1,1149,1150,1151,-1,1152,1153,1154,-1,1155,1156,1157,-1,1158,1159,1160,-1,1161,1162,1163,-1,1164,1165,1166,-1,1167,1168,1169,-1,1170,1171,1172,-1,1173,1174,1175,-1,1176,1177,1178,-1,1179,1180,1181,-1,1182,1183,1184,-1,1185,1186,1187,-1,1188,1189,1190,-1,1191,1192,1193,-1,1194,1195,1196,-1,1197,1198,1199,-1,1200,1201,1202,-1,1203,1204,1205,-1,1206,1207,1208,-1,1209,1210,1211,-1,1212,1213,1214,-1,1215,1216,1217,-1,1218,1219,1220,-1,1221,1222,1223,-1,1224,1225,1226,-1,1227,1228,1229,-1,1230,1231,1232,-1,1233,1234,1235,-1,1236,1237,1238,-1,1239,1240,1241,-1,1242,1243,1244,-1,1245,1246,1247,-1,1248,1249,1250,-1,1251,1252,1253,-1,1254,1255,1256,-1,1257,1258,1259,-1,1260,1261,1262,-1,1263,1264,1265,-1,1266,1267,1268,-1,1269,1270,1271,-1,1272,1273,1274,-1,1275,1276,1277,-1,1278,1279,1280,-1,1281,1282,1283,-1,1284,1285,1286,-1,1287,1288,1289,-1,1290,1291,1292,-1,1293,1294,1295,-1,1296,1297,1298,-1,1299,1300,1301,-1,1302,1303,1304,-1,1305,1306,1307,-1,1308,1309,1310,-1,1311,1312,1313,-1,1314,1315,1316,-1,1317,1318,1319,-1,1320,1321,1322,-1,1323,1324,1325,-1,1326,1327,1328,-1,1329,1330,1331,-1,1332,1333,1334,-1,1335,1336,1337,-1,1338,1339,1340,-1,1341,1342,1343,-1,1344,1345,1346,-1,1347,1348,1349,-1,1350,1351,1352,-1,1353,1354,1355,-1,1356,1357,1358,-1,1359,1360,1361,-1,1362,1363,1364,-1,1365,1366,1367,-1,1368,1369,1370,-1,1371,1372,1373,-1,1374,1375,1376,-1,1377,1378,1379,-1,1380,1381,1382,-1,1383,1384,1385,-1,1386,1387,1388,-1,1389,1390,1391,-1,1392,1393,1394,-1,1395,1396,1397,-1,1398,1399,1400,-1,1401,1402,1403,-1,1404,1405,1406,-1,1407,1408,1409,-1,1410,1411,1412,-1,1413,1414,1415,-1,1416,1417,1418,-1,1419,1420,1421,-1,1422,1423,1424,-1,1425,1426,1427,-1,1428,1429,1430,-1,1431,1432,1433,-1,1434,1435,1436,-1,1437,1438,1439,-1,1440,1441,1442,-1,1443,1444,1445,-1,1446,1447,1448,-1,1449,1450,1451,-1,1452,1453,1454,-1,1455,1456,1457,-1,1458,1459,1460,-1,1461,1462,1463,-1,1464,1465,1466,-1,1467,1468,1469,-1,1470,1471,1472,-1,1473,1474,1475,-1,1476,1477,1478,-1,1479,1480,1481,-1,1482,1483,1484,-1,1485,1486,1487,-1,1488,1489,1490,-1,1491,1492,1493,-1,1494,1495,1496,-1,1497,1498,1499,-1,1500,1501,1502,-1,1503,1504,1505,-1,1506,1507,1508,-1,1509,1510,1511,-1,1512,1513,1514,-1,1515,1516,1517,-1,1518,1519,1520,-1,1521,1522,1523,-1,1524,1525,1526,-1,1527,1528,1529,-1,1530,1531,1532,-1,1533,1534,1535,-1,1536,1537,1538,-1,1539,1540,1541,-1,1542,1543,1544,-1,1545,1546,1547,-1,1548,1549,1550,-1,1551,1552,1553,-1,1554,1555,1556,-1,1557,1558,1559,-1,1560,1561,1562,-1,1563,1564,1565,-1,1566,1567,1568,-1,1569,1570,1571,-1,1572,1573,1574,-1,1575,1576,1577,-1,1578,1579,1580,-1,1581,1582,1583,-1,1584,1585,1586,-1,1587,1588,1589,-1,1590,1591,1592,-1,1593,1594,1595,-1,1596,1597,1598,-1,1599,1600,1601,-1,1602,1603,1604,-1,1605,1606,1607,-1,1608,1609,1610,-1,1611,1612,1613,-1,1614,1615,1616,-1,1617,1618,1619,-1,1620,1621,1622,-1,1623,1624,1625,-1,1626,1627,1628,-1,1629,1630,1631,-1,1632,1633,1634,-1,1635,1636,1637,-1,1638,1639,1640,-1,1641,1642,1643,-1,1644,1645,1646,-1,1647,1648,1649,-1,1650,1651,1652,-1,1653,1654,1655,-1,1656,1657,1658,-1,1659,1660,1661,-1,1662,1663,1664,-1,1665,1666,1667,-1,1668,1669,1670,-1,1671,1672,1673,-1,1674,1675,1676,-1,1677,1678,1679,-1,1680,1681,1682,-1,1683,1684,1685,-1,1686,1687,1688,-1,1689,1690,1691,-1,1692,1693,1694,-1,1695,1696,1697,-1,1698,1699,1700,-1,1701,1702,1703,-1,1704,1705,1706,-1,1707,1708,1709,-1,1710,1711,1712,-1,1713,1714,1715,-1,1716,1717,1718,-1,1719,1720,1721,-1,1722,1723,1724,-1,1725,1726,1727,-1,1728,1729,1730,-1,1731,1732,1733,-1,1734,1735,1736,-1,1737,1738,1739,-1,1740,1741,1742,-1,1743,1744,1745,-1,1746,1747,1748,-1,1749,1750,1751,-1,1752,1753,1754,-1,1755,1756,1757,-1,1758,1759,1760,-1,1761,1762,1763,-1,1764,1765,1766,-1,1767,1768,1769,-1,1770,1771,1772,-1,1773,1774,1775,-1,1776,1777,1778,-1,1779,1780,1781,-1,1782,1783,1784,-1,1785,1786,1787,-1,1788,1789,1790,-1,1791,1792,1793,-1,1794,1795,1796,-1,1797,1798,1799,-1,1800,1801,1802,-1,1803,1804,1805,-1,1806,1807,1808,-1,1809,1810,1811,-1,1812,1813,1814,-1,1815,1816,1817,-1,1818,1819,1820,-1,1821,1822,1823,-1,1824,1825,1826,-1,1827,1828,1829,-1,1830,1831,1832,-1,1833,1834,1835,-1,1836,1837,1838,-1,1839,1840,1841,-1,1842,1843,1844,-1,1845,1846,1847,-1,1848,1849,1850,-1,1851,1852,1853,-1,1854,1855,1856,-1,1857,1858,1859,-1,1860,1861,1862,-1,1863,1864,1865,-1,1866,1867,1868,-1,1869,1870,1871,-1,1872,1873,1874,-1,1875,1876,1877,-1,1878,1879,1880,-1,1881,1882,1883,-1,1884,1885,1886,-1,1887,1888,1889,-1,1890,1891,1892,-1,1893,1894,1895,-1,1896,1897,1898,-1,1899,1900,1901,-1,1902,1903,1904,-1,1905,1906,1907,-1,1908,1909,1910,-1,1911,1912,1913,-1,1914,1915,1916,-1,1917,1918,1919,-1,1920,1921,1922,-1,1923,1924,1925,-1,1926,1927,1928,-1,1929,1930,1931,-1,1932,1933,1934,-1,1935,1936,1937,-1,1938,1939,1940,-1,1941,1942,1943,-1,1944,1945,1946,-1,1947,1948,1949,-1,1950,1951,1952,-1,1953,1954,1955,-1,1956,1957,1958,-1,1959,1960,1961,-1,1962,1963,1964,-1,1965,1966,1967,-1,1968,1969,1970,-1,1971,1972,1973,-1,1974,1975,1976,-1,1977,1978,1979,-1,1980,1981,1982,-1,1983,1984,1985,-1,1986,1987,1988,-1,1989,1990,1991,-1,1992,1993,1994,-1,1995,1996,1997,-1,1998,1999,2000,-1,2001,2002,2003,-1,2004,2005,2006,-1,2007,2008,2009,-1,2010,2011,2012,-1,2013,2014,2015,-1,2016,2017,2018,-1,2019,2020,2021,-1,2022,2023,2024,-1,2025,2026,2027,-1,2028,2029,2030,-1,2031,2032,2033,-1,2034,2035,2036,-1,2037,2038,2039,-1,2040,2041,2042,-1,2043,2044,2045,-1,2046,2047,2048,-1,2049,2050,2051,-1,2052,2053,2054,-1,2055,2056,2057,-1,2058,2059,2060,-1,2061,2062,2063,-1,2064,2065,2066,-1,2067,2068,2069,-1,2070,2071,2072,-1,2073,2074,2075,-1,2076,2077,2078,-1,2079,2080,2081,-1,2082,2083,2084,-1,2085,2086,2087,-1,2088,2089,2090,-1,2091,2092,2093,-1,2094,2095,2096,-1,2097,2098,2099,-1,2100,2101,2102,-1,2103,2104,2105,-1,2106,2107,2108,-1,2109,2110,2111,-1,2112,2113,2114,-1,2115,2116,2117,-1,2118,2119,2120,-1,2121,2122,2123,-1,2124,2125,2126,-1,2127,2128,2129,-1,2130,2131,2132,-1,2133,2134,2135,-1,2136,2137,2138,-1,2139,2140,2141,-1,2142,2143,2144,-1,2145,2146,2147,-1,2148,2149,2150,-1,2151,2152,2153,-1,2154,2155,2156,-1,2157,2158,2159,-1,2160,2161,2162,-1,2163,2164,2165,-1,2166,2167,2168,-1,2169,2170,2171,-1,2172,2173,2174,-1,2175,2176,2177,-1,2178,2179,2180,-1,2181,2182,2183,-1,2184,2185,2186,-1,2187,2188,2189,-1,2190,2191,2192,-1,2193,2194,2195,-1,2196,2197,2198,-1,2199,2200,2201,-1,2202,2203,2204,-1,2205,2206,2207,-1,2208,2209,2210,-1,2211,2212,2213,-1,2214,2215,2216,-1,2217,2218,2219,-1,2220,2221,2222,-1,2223,2224,2225,-1,2226,2227,2228,-1,2229,2230,2231,-1,2232,2233,2234,-1,2235,2236,2237,-1,2238,2239,2240,-1,2241,2242,2243,-1,2244,2245,2246,-1,2247,2248,2249,-1,2250,2251,2252,-1,2253,2254,2255,-1,2256,2257,2258,-1,2259,2260,2261,-1,2262,2263,2264,-1,2265,2266,2267,-1,2268,2269,2270,-1,2271,2272,2273,-1,2274,2275,2276,-1,2277,2278,2279,-1,2280,2281,2282,-1,2283,2284,2285,-1,2286,2287,2288,-1,2289,2290,2291,-1,2292,2293,2294,-1,2295,2296,2297,-1,2298,2299,2300,-1,2301,2302,2303,-1,2304,2305,2306,-1,2307,2308,2309,-1,2310,2311,2312,-1,2313,2314,2315,-1,2316,2317,2318,-1,2319,2320,2321,-1,2322,2323,2324,-1,2325,2326,2327,-1,2328,2329,2330,-1,2331,2332,2333,-1,2334,2335,2336,-1,2337,2338,2339,-1,2340,2341,2342,-1,2343,2344,2345,-1,2346,2347,2348,-1,2349,2350,2351,-1,2352,2353,2354,-1,2355,2356,2357,-1,2358,2359,2360,-1,2361,2362,2363,-1,2364,2365,2366,-1,2367,2368,2369,-1,2370,2371,2372,-1,2373,2374,2375,-1,2376,2377,2378,-1,2379,2380,2381,-1,2382,2383,2384,-1,2385,2386,2387,-1,2388,2389,2390,-1,2391,2392,2393,-1,2394,2395,2396,-1,2397,2398,2399,-1,2400,2401,2402,-1,2403,2404,2405,-1,2406,2407,2408,-1,2409,2410,2411,-1,2412,2413,2414,-1,2415,2416,2417,-1,2418,2419,2420,-1,2421,2422,2423,-1,2424,2425,2426,-1,2427,2428,2429,-1,2430,2431,2432,-1,2433,2434,2435,-1,2436,2437,2438,-1,2439,2440,2441,-1,2442,2443,2444,-1,2445,2446,2447,-1,2448,2449,2450,-1,2451,2452,2453,-1,2454,2455,2456,-1,2457,2458,2459,-1,2460,2461,2462,-1,2463,2464,2465,-1,2466,2467,2468,-1,2469,2470,2471,-1,2472,2473,2474,-1,2475,2476,2477,-1,2478,2479,2480,-1,2481,2482,2483,-1,2484,2485,2486,-1,2487,2488,2489,-1,2490,2491,2492,-1,2493,2494,2495,-1,2496,2497,2498,-1,2499,2500,2501,-1,2502,2503,2504,-1,2505,2506,2507,-1,2508,2509,2510,-1,2511,2512,2513,-1,2514,2515,2516,-1,2517,2518,2519,-1,2520,2521,2522,-1,2523,2524,2525,-1,2526,2527,2528,-1,2529,2530,2531,-1,2532,2533,2534,-1,2535,2536,2537,-1,2538,2539,2540,-1,2541,2542,2543,-1,2544,2545,2546,-1,2547,2548,2549,-1,2550,2551,2552,-1,2553,2554,2555,-1,2556,2557,2558,-1,2559,2560,2561,-1,2562,2563,2564,-1,2565,2566,2567,-1,2568,2569,2570,-1,2571,2572,2573,-1,2574,2575,2576,-1,2577,2578,2579,-1,2580,2581,2582,-1,2583,2584,2585,-1,2586,2587,2588,-1,2589,2590,2591,-1,2592,2593,2594,-1,2595,2596,2597,-1,2598,2599,2600,-1,2601,2602,2603,-1,2604,2605,2606,-1,2607,2608,2609,-1,2610,2611,2612,-1,2613,2614,2615,-1,2616,2617,2618,-1,2619,2620,2621,-1,2622,2623,2624,-1,2625,2626,2627,-1,2628,2629,2630,-1,2631,2632,2633,-1,2634,2635,2636,-1,2637,2638,2639,-1,2640,2641,2642,-1,2643,2644,2645,-1,2646,2647,2648,-1,2649,2650,2651,-1,2652,2653,2654,-1,2655,2656,2657,-1,2658,2659,2660,-1,2661,2662,2663,-1,2664,2665,2666,-1,2667,2668,2669,-1,2670,2671,2672,-1,2673,2674,2675,-1,2676,2677,2678,-1,2679,2680,2681,-1,2682,2683,2684,-1,2685,2686,2687,-1,2688,2689,2690,-1,2691,2692,2693,-1,2694,2695,2696,-1,2697,2698,2699,-1,2700,2701,2702,-1,2703,2704,2705,-1,2706,2707,2708,-1,2709,2710,2711,-1,2712,2713,2714,-1,2715,2716,2717,-1,2718,2719,2720,-1,2721,2722,2723,-1,2724,2725,2726,-1,2727,2728,2729,-1,2730,2731,2732,-1,2733,2734,2735,-1,2736,2737,2738,-1,2739,2740,2741,-1,2742,2743,2744,-1,2745,2746,2747,-1,2748,2749,2750,-1,2751,2752,2753,-1,2754,2755,2756,-1,2757,2758,2759,-1,2760,2761,2762,-1,2763,2764,2765,-1,2766,2767,2768,-1,2769,2770,2771,-1,2772,2773,2774,-1,2775,2776,2777,-1,2778,2779,2780,-1,2781,2782,2783,-1,2784,2785,2786,-1,2787,2788,2789,-1,2790,2791,2792,-1,2793,2794,2795,-1,2796,2797,2798,-1,2799,2800,2801,-1,2802,2803,2804,-1,2805,2806,2807,-1,2808,2809,2810,-1,2811,2812,2813,-1,2814,2815,2816,-1,2817,2818,2819,-1,2820,2821,2822,-1,2823,2824,2825,-1,2826,2827,2828,-1,2829,2830,2831,-1,2832,2833,2834,-1,2835,2836,2837,-1,2838,2839,2840,-1,2841,2842,2843,-1,2844,2845,2846,-1,2847,2848,2849,-1,2850,2851,2852,-1,2853,2854,2855,-1,2856,2857,2858,-1,2859,2860,2861,-1,2862,2863,2864,-1,2865,2866,2867,-1,2868,2869,2870,-1,2871,2872,2873,-1,2874,2875,2876,-1,2877,2878,2879,-1]
IndexedFaceSet31.solid = False
Coordinate32 = x3d.Coordinate()

IndexedFaceSet31.coord = Coordinate32
Normal33 = x3d.Normal()

IndexedFaceSet31.normal = Normal33

Shape28.geometry = IndexedFaceSet31

Transform27.children.append(Shape28)
Billboard34 = x3d.Billboard()
Transform35 = x3d.Transform()
Transform35.DEF = "violin"
Transform35.rotation = [1,0,0,-0.5]
Transform35.scale = [100,100,100]
Transform35.translation = [0,100,0]
Shape36 = x3d.Shape()
Appearance37 = x3d.Appearance()
Material38 = x3d.Material()
Material38.ambientIntensity = 0.0933
Material38.diffuseColor = [0.345,0.345,0.882]
Material38.shininess = 0.51
Material38.specularColor = [0.46,0.46,0.46]

Appearance37.material = Material38

Shape36.appearance = Appearance37
Text39 = x3d.Text()
Text39.string = ["Sound Source"]
FontStyle40 = x3d.FontStyle()
FontStyle40.family = ["Times","SERIF"]
FontStyle40.style = "BOLD"

Text39.fontStyle = FontStyle40

Shape36.geometry = Text39

Transform35.children.append(Shape36)

Billboard34.children.append(Transform35)

Transform27.children.append(Billboard34)

Scene15.children.append(Transform27)
AudioDestination41 = x3d.AudioDestination()
AudioDestination41.channelCountMode = "MAX"
AudioDestination41.channelInterpretation = "SPEAKERS"
#not allowed here <Transform USE='Audio1'/>
SpatialSound42 = x3d.SpatialSound()
SpatialSound42.coneInnerAngle = 6.283
SpatialSound42.coneOuterAngle = 6.283
SpatialSound42.enableHRTF = True
SpatialSound42.distanceModel = "INVERSE"

AudioDestination41.children.append(SpatialSound42)
BufferAudioSource43 = x3d.BufferAudioSource()
BufferAudioSource43.loop = True
BufferAudioSource43.pauseTime = -1
BufferAudioSource43.resumeTime = -1
BufferAudioSource43.stopTime = -1
BufferAudioSource43.url = ["sound/saxophone.mp3","sound/saxophone.ogg"]
BufferAudioSource43.channelCountMode = "MAX"
BufferAudioSource43.channelInterpretation = "SPEAKERS"

AudioDestination41.children.append(BufferAudioSource43)

Scene15.children.append(AudioDestination41)

X3D0.Scene = Scene15
f = open("././SingleAudio_RoundTrip.x3d", mode="w", encoding="utf-8")
f.write(X3D0.XML())
f.close()
