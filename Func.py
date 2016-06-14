import xml.etree.ElementTree as ET
import webbrowser
import gmail
tag_list, field_list, value_list = [""], [""], [""]



def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

def daily(note):
    # global list_group
    global tag_list,field_list,value_list
    print(note.findtext("boxofficeType"))
    print(note.findtext("showRange"))

    tag_list=["순번","일일 순위","순위증감","랭킹신규진입","영화대표코드","영화제목",
              "개봉일","매출액","매출지분율","매출액 증감분","매출액 증감률","누적매출액","관람객수",
              "관람객 증감분", "관람객 증감비율","누적관객","상영스크린수","상영횟수"]
    field_list=["rnum","rank","rankInten","rankOldAndNew","movieCd","movieNm","openDt","salesAmt","salesShare"
                ,"salesInten","salesChange","salesAcc","audiCnt","audiInten","audiChange","audiAcc","scrnCnt",
                "showCnt"]
    value_list=[]

    for element in note.findall("dailyBoxOfficeList"):
        for tag in element.findall("dailyBoxOffice"):
            index = 0
            while index<len(tag_list):
                value_list.append(tag.findtext(field_list[index]))
                print(tag_list[index]," --> ",tag.findtext(field_list[index]))
                index+=1


            # print("순번\t\t\t\t\t", tag.findtext("rnum"))
            # print("일일 박스오피스 순위\t", tag.findtext("rank"))
            # print("전일대비 순위증감\t\t", tag.findtext("rankInten"))
            # print("랭킹신규진입\t\t\t", tag.findtext("rankOldAndNew"))
            # print("영화대표코드\t\t\t", tag.findtext("movieCd"))
            # print("영화제목\t\t\t\t", tag.findtext("movieNm"))
            # print("개봉일\t\t\t\t\t", tag.findtext("openDt"))
            # print("매출액\t\t\t\t\t", tag.findtext("salesAmt"))
            # print("매출지분율\t\t\t\t", tag.findtext("salesShare"))
            # print("매출액 증감분\t\t\t", tag.findtext("salesInten"))
            # print("매출액 증감률\t\t\t", tag.findtext("salesChange"))
            # print("누적매출액\t\t\t\t", tag.findtext("salesAcc"))
            # print("관람객수\t\t\t\t", tag.findtext("audiCnt"))
            # print("관람객 증감분\t\t\t", tag.findtext("audiInten"))
            # print("관람객 증감비율\t\t\t", tag.findtext("audiChange"))
            # print("누적관객\t\t\t\t", tag.findtext("audiAcc"))
            # print("상영스크린수\t\t\t", tag.findtext("scrnCnt"))
            # print("상영횟수\t\t\t\t", tag.findtext("showCnt"))
            # 공백용
            print()
    # print(tag_list)

def weekly(note):
    print(note.findtext("boxofficeType"))
    print(note.findtext("showRange"))
    for element in note.findall("weeklyBoxOfficeList"):
        for tag in element.findall("weeklyBoxOffice"):
            print("순번\t\t\t\t\t",tag.findtext("rnum"))
            print("주간/주말 순위\t\t\t",tag.findtext("rank"))
            print("전주대비 순위증감\t\t",tag.findtext("rankInten"))
            print("랭킹신규진입\t\t\t",tag.findtext("rankOldAndNew"))
            print("영화대표코드\t\t\t", tag.findtext("movieCd"))
            print("영화제목\t\t\t\t", tag.findtext("movieNm"))
            print("개봉일\t\t\t\t\t", tag.findtext("openDt"))
            print("매출액\t\t\t\t\t", tag.findtext("salesAmt"))
            print("매출지분율\t\t\t\t", tag.findtext("salesShare"))
            print("매출액 증감분\t\t\t", tag.findtext("salesInten"))
            print("매출액 증감률\t\t\t", tag.findtext("salesChange"))
            print("누적매출액\t\t\t\t", tag.findtext("salesAcc"))
            print("관람객수\t\t\t\t", tag.findtext("audiCnt"))
            print("관람객 증감분\t\t\t", tag.findtext("audiInten"))
            print("관람객 증감비율\t\t\t", tag.findtext("audiChange"))
            print("누적관객\t\t\t\t", tag.findtext("audiAcc"))
            print("상영스크린수\t\t\t", tag.findtext("scrnCnt"))
            print("상영횟수\t\t\t\t", tag.findtext("showCnt"))
            #공백용
            print()

def MovieList(note):
    for element in note.findall("movieList"):
        for tag in element.findall("movie"):
            print("영화대표코드\t\t", tag.findtext("movieCd"))
            print("영화명(국)\t\t\t", tag.findtext("movieNm"))
            print("영화명(외)\t\t\t", tag.findtext("movieNmEn"))
            print("제작연도\t\t\t", tag.findtext("prdtYear"))
            print("개봉연도\t\t\t", tag.findtext("openDt"))
            print("영화유형\t\t\t", tag.findtext("typeNm"))
            print("제작상태\t\t\t", tag.findtext("prdtStatNm"))
            print("제작국가\t\t\t", tag.findtext("nationAlt"))
            print("영화장르\t\t\t", tag.findtext("genreAlt"))
            print("대표 제작국가명\t\t", tag.findtext("repNationNm"))
            print("대표 장르명\t\t\t", tag.findtext("repGenreNm"))

            # print("상영스크린수\t\t\t", tag.findtext("peopleNm"))

            # print("상영횟수\t\t\t\t", tag.findtext("companyCd"))
            # print("상영횟수\t\t\t\t", tag.findtext("companyNm"))
            # 공백용
            print()

def CompanyList(note):
    for element in note.findall("companyList"):
        for tag in element.findall("company"):
            print("영화사 코드\t\t\t", tag.findtext("companyCd"))
            print("영화사명(국)\t\t", tag.findtext("companyNm"))
            print("영화사명(외)\t\t", tag.findtext("companyNmEn"))
            print("영화사 분류\t\t\t", tag.findtext("companyPartNames"))
            print("대표자명\t\t\t", tag.findtext("ceoNm"))

            print()
def ConnectCinema():
    print("원하는 극장 홈페이지 선택")
    sel=int(input("1.CGV 2.메가박스 3. 롯데시네마"))
    if(sel==1):
        site='www.cgv.co.kr'
    elif(sel==2):
        site='www.megabox.co.kr'
    elif(sel==3):
        site='www.lottecinema.co.kr'

    webbrowser.open_new(site)


