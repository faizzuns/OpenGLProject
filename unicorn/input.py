import sys
import json
import random


li = [244,445,327,455,277,481,277,481,201,495,244,445,201,495,277,481,230,564,230,564,201,459,151,703,151,703,230,564,239,646,239,646,151,703,189,723,189,723,151,703,189,787,151,703,149,783,94,721,94,721,151,703,108,646,108,646,151,703,170,618,170,618,108,646,114,573,114,573,170,618,201,459,108,646,81,649,112,594,225,468,167,495,154,539,
        346,1016,318,1025,322,997,322,977,318,1025,283,1019,283,1019,322,977,254,994,254,994,267,1004,230,1017,230,1017,254,994,208,1002,
        254,994,208,1002,183,925,183,925,254,994,245,943,245,943,183,925,215,879,215,879,183,925,212,831,313,799,342,763,447,712,342,763,447,712,454,668,342,763,390,652,454,668,447,712,454,668,504,671,
        322,977,254,994,245,943,245,943,322,977,298,943,245,943,298,943,215,879,215,879,298,943,278,874,215,879,278,874,283,830,215,879,283,830,210,796,210,796,283,830,241,767,241,767,283,767,313,799,241,767,313,799,277,711,277,710,313,799,342,763,277,710,342,763,390,652,390,652,277,710,244,445,
        342,763,390,652,230,564,230,564,390,652,277,481,277,481,390,652,357,439,357,440,390,652,450,415,450,415,390,652,454,668,450,415,454,668,575,674,575,674,450,415,648,524,648,524,575,674,698,650,698,650,648,524,728,565,728,565,698,650,757,629,757,629,698,650,733,703,733,703,757,629,798,707,733,703,798,707,700,753,798,709,700,753,695,803,700,753,695,803,650,746,650,746,695,803,624,794,650,746,624,794,633,731,633,731,624,794,590,758,590,758,624,794,585,785,633,354,638,281,822,217,633,354,822,217,781,274,822,217,690,225,725,251,822,217,781,274,903,257,822,217,903,257,961,230,724,192,830,180,822,217,822,217,830,180,847,219,830,180,847,219,930,195,930,195,847,219,961,230,903,257,961,230,1012,272,1012,272,961,230,1020,256,1020,256,973,213,986,241,1020,256,1012,271,1064,346,1064,346,1020,256,1063,304,1074,381,1119,386,1074,397,1074,397,1122,409,1067,414,1067,414,1109,447,1058,440,1067,414,1109,447,1198,473,1109,447,1198,473,1230,496,1058,440,1109,447,1193,487,1193,487,1109,447,1230,496,978,423,976,455,970,441,978,423,976,455,994,453,897,568,908,559,919,569,897,568,904,569,898,579,940,572,879,568,917,590,879,568,917,590,900,591,879,568,900,591,881,583,879,568,888,518,873,534,879,568,888,518,940,572,940,572,888,518,945,480,945,489,888,518,903,461,945,480,1008,484,940,572,945,480,1008,484,982,383,1008,484,982,383,1052,459,982,383,945,480,903,461,903,461,982,383,903,428,903,428,982,383,910,350,910,350,1012,272,982,383,1012,272,982,383,1064,346,1064,346,982,383,1074,381,982,383,1074,381,1052,459,910,350,1012,272,903,257,903,257,910,350,781,274,781,274,910,350,873,459,781,274,910,350,903,428,781,274,854,421,633,354,854,421,633,354,756,628,633,354,728,567,561,397,728,567,561,397,450,414,854,421,756,628,873,459,873,459,756,628,869,528,756,628,869,528,845,579,845,579,756,628,834,670,845,579,834,670,880,638,834,670,880,638,839,688,880,638,839,688,904,670,839,688,904,670,890,710,839,688,890,710,876,720,839,688,876,720,841,779,839,688,841,779,806,734,841,779,806,734,834,793,806,734,834,793,818,799,806,734,818,799,746,806,806,734,746,806,766,736,746,806,766,736,748,754]

with open('input.json', 'w') as f:
    data = {}
    i = 0
    for x in range(0, len(li), 6):
        data[i] = {}
        data[i][0] = [li[x], li[x+1]]
        data[i][1] = [li[x+2], li[x+3]]
        data[i][2] = [li[x+4], li[x+5]]
        i = i + 1

    json.dump(data, f)
