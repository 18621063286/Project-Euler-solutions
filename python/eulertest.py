# 
# Test suite for Project Euler all Python solutions
# Copyright (c) Project Nayuki. All rights reserved.
# 
# https://www.nayuki.io/page/project-euler-solutions
# https://github.com/nayuki/Project-Euler-solutions
# 

import importlib, time


def main():
	totaltime = 0.0  # In seconds
	for (prob, expectans) in sorted(ANSWERS.items()):
		module = importlib.import_module("p{:03d}".format(prob))
		starttime = time.time()
		actualans = module.compute()  # Must return a string
		elapsedtime = time.time() - starttime
		totaltime += elapsedtime
		print("Problem {:03d}: {:7d} ms{}".format(
			prob, int(round(elapsedtime * 1000)),
			"" if actualans == expectans else "    *** FAIL ***"))
	print("Total computation time: {} ms".format(int(round(totaltime * 1000))))


ANSWERS = {
	  1: "233168",
	  2: "4613732",
	  3: "6857",
	  4: "906609",
	  5: "232792560",
	  6: "25164150",
	  7: "104743",
	  8: "23514624000",
	  9: "31875000",
	 10: "142913828922",
	 11: "70600674",
	 12: "76576500",
	 13: "5537376230",
	 14: "837799",
	 15: "137846528820",
	 16: "1366",
	 17: "21124",
	 18: "1074",
	 19: "171",
	 20: "648",
	 21: "31626",
	 22: "871198282",
	 23: "4179871",
	 24: "2783915460",
	 25: "4782",
	 26: "983",
	 27: "-59231",
	 28: "669171001",
	 29: "9183",
	 30: "443839",
	 31: "73682",
	 32: "45228",
	 33: "100",
	 34: "40730",
	 35: "55",
	 36: "872187",
	 37: "748317",
	 38: "932718654",
	 39: "840",
	 40: "210",
	 41: "7652413",
	 42: "162",
	 43: "16695334890",
	 44: "5482660",
	 45: "1533776805",
	 46: "5777",
	 47: "134043",
	 48: "9110846700",
	 49: "296962999629",
	 50: "997651",
	 51: "121313",
	 52: "142857",
	 53: "4075",
	 54: "376",
	 55: "249",
	 56: "972",
	 57: "153",
	 58: "26241",
	 59: "107359",
	 60: "26033",
	 61: "28684",
	 62: "127035954683",
	 63: "49",
	 64: "1322",
	 65: "272",
	 66: "661",
	 67: "7273",
	 68: "6531031914842725",
	 69: "510510",
	 70: "8319823",
	 71: "428570",
	 72: "303963552391",
	 73: "7295372",
	 74: "402",
	 75: "161667",
	 76: "190569291",
	 77: "71",
	 78: "55374",
	 79: "73162890",
	 80: "40886",
	 81: "427337",
	 82: "260324",
	 83: "425185",
	 84: "101524",
	 85: "2772",
	 86: "1818",
	 87: "1097343",
	 88: "7587457",
	 89: "743",
	 90: "1217",
	 91: "14234",
	 92: "8581146",
	 93: "1258",
	 94: "518408346",
	 95: "14316",
	 96: "24702",
	 97: "8739992577",
	 98: "18769",
	 99: "709",
	100: "756872327473",
	101: "37076114526",
	102: "228",
	104: "329468",
	105: "73702",
	107: "259679",
	108: "180180",
	109: "38182",
	111: "612407567715",
	112: "1587000",
	113: "51161058134250",
	114: "16475640049",
	115: "168",
	116: "20492570929",
	117: "100808458960497",
	118: "44680",
	119: "248155780267521",
	120: "333082500",
	121: "2269",
	122: "1582",
	123: "21035",
	124: "21417",
	125: "2906969179",
	127: "18407904",
	128: "14516824220",
	129: "1000023",
	130: "149253",
	132: "843296",
	133: "453647705",
	134: "18613426663617118",
	135: "4989",
	139: "10057761",
	142: "1006193",
	145: "608720",
	146: "676333270",
	149: "52852124",
	150: "-271248680",
	151: "0.464399",
	155: "3857447",
	160: "16576",
	162: "3D58725572C62302",
	164: "378158756814587",
	166: "7130034",
	169: "178653872807",
	171: "142989277",
	172: "227485267000992000",
	173: "1572729",
	174: "209566",
	178: "126461847755",
	179: "986262",
	182: "399788195976",
	186: "2325629",
	187: "17427258",
	188: "95962097",
	191: "1918080160",
	197: "1.710637717",
	203: "34029210557338",
	204: "2944730",
	205: "0.5731441",
	206: "1389019170",
	208: "331951449665644800",
	211: "1922364685",
	214: "1677366278943",
	215: "806844323190414",
	216: "5437849",
	218: "0",
	222: "1590933",
	225: "2009",
	231: "7526965179680",
	243: "892371480",
	249: "9275262564250418",
	250: "1425480602091519",
	265: "209110240768",
	267: "0.999992836187",
	271: "4617456485273129588",
	280: "430.088247",
	287: "313135496",
	301: "2178309",
	303: "1111981904675169",
	304: "283988410192",
	315: "13625242",
	323: "6.3551758451",
	329: "199740353/29386561536000",
	345: "13938",
	346: "336108797689259276",
	347: "11109800204052",
	348: "1004195061",
	357: "1739023853137",
	381: "139602943319822",
	387: "696067597313468",
	401: "281632621",
	407: "39782849136421",
	425: "46479497324",
	429: "98792821",
	451: "153651073760956",
	493: "6.818741802",
	500: "35407281",
	518: "100315739184392",
	549: "476001479068717",
	587: "2240",
}


if __name__ == "__main__":
	main()
