"""PPI series configuration - FRED Producer Price Index series organized by industry category."""

CATEGORIES = {
    "Semiconductor & Electronics": {
        "series": {
            "Semiconductor Manufacturing": {
                "id": "PCU334413334413",
                "kr_stocks": "삼성전자, SK하이닉스, DB하이텍, 리노공업",
                "drivers": "AI/HBM 수요 폭증 → 파운드리 가동률 상승 → 웨이퍼 가격 인상",
                "risks": "AI 투자 사이클 둔화, 중국 반도체 자급률 확대 → 공급 과잉 → 가격 하락"
            },
            "Electronic Component Mfg": {
                "id": "PCU334414334414",
                "kr_stocks": "삼성전기, LG이노텍, 대덕전자",
                "drivers": "스마트폰/AI서버 MLCC 수요 증가 → 부품 단가 인상",
                "risks": "스마트폰 출하량 둔화, 중국 MLCC 업체 저가 공세 → 가격 경쟁 심화"
            },
            "Printed Circuit Board Mfg": {
                "id": "PCU334412334412",
                "kr_stocks": "대덕전자, 심텍, ISC",
                "drivers": "AI서버용 고다층 PCB 수요 급증 → 원자재(동박적층판) 가격 상승",
                "risks": "서버 투자 사이클 정점 통과 시 수요 급감, 중국 PCB 증설 물량 출회"
            },
            "Electronic Connector Mfg": {
                "id": "PCU334417334417",
                "kr_stocks": "이수페타시스, 비에이치",
                "drivers": "고속 데이터 전송 수요 → 고사양 커넥터 단가 상승",
                "risks": "전방 IT 수요 둔화, 범용 커넥터 가격 하락 압력"
            },
        }
    },
    "Electrical & Power Infrastructure": {
        "series": {
            "Transformer Manufacturing": {
                "id": "PCU335311335311",
                "kr_stocks": "LS ELECTRIC, HD현대일렉트릭, 일진전기, 제룡전기",
                "drivers": "AI 데이터센터 전력 수요 폭증 → 변압기 글로벌 백로그 사상 최대 → 납기 2~3년 대기",
                "risks": "데이터센터 투자 속도 조절, 전력망 투자 예산 삭감 → 수주 감소"
            },
            "Electrical Equipment Mfg": {
                "id": "PCU335313335313",
                "kr_stocks": "LS ELECTRIC, HD현대일렉트릭, 일진전기, 제룡전기",
                "drivers": "글로벌 전력 인프라 노후화 교체 + 재생에너지 연계 수요 → 수배전 설비 가격 상승",
                "risks": "각국 재생에너지 보조금 축소, 금리 상승 → 인프라 투자 지연"
            },
            "Switchgear & Switchboard Mfg": {
                "id": "PCU335313335313A",
                "kr_stocks": "LS ELECTRIC, HD현대일렉트릭, 일진전기, 제룡전기",
                "drivers": "데이터센터/EV 충전 인프라 확대 → 수배전반 수요 증가 → 원자재(구리) 가격 전가",
                "risks": "구리 가격 급락 시 단가 인하 압력, 중국산 저가 제품 유입"
            },
            "Power & Distribution Transformers": {
                "id": "PCU335311335311A",
                "kr_stocks": "LS ELECTRIC, HD현대일렉트릭, 일진전기, 제룡전기",
                "drivers": "미국 IRA/인프라법 → 전력망 현대화 투자 확대 → 배전용 변압기 수요 급증",
                "risks": "미국 정책 변경(IRA 축소), 변압기 증설 완료 후 공급 정상화"
            },
            "Motor & Generator Mfg": {
                "id": "PCU335312335312",
                "kr_stocks": "현대일렉트릭, 효성중공업",
                "drivers": "산업용 전동기 교체 수요 + 재생에너지 발전기 수요 증가",
                "risks": "제조업 경기 침체 → 설비투자 감소 → 수요 위축"
            },
        }
    },
    "Energy & Turbines": {
        "series": {
            "Turbine & Power Generation Equipment": {
                "id": "PCU333611333611",
                "kr_stocks": "두산에너빌리티, 한화파워시스템",
                "drivers": "가스터빈 수요 증가(AI 전력+탈석탄) → 장비 단가 인상 → 부품 가격 상승",
                "risks": "재생에너지 가격 하락으로 가스발전 경쟁력 약화, 원전 정책 전환"
            },
            "Oil & Gas Field Machinery": {
                "id": "PCU333132333132",
                "kr_stocks": "두산에너빌리티, TKC",
                "drivers": "유가 고유지 → E&P 투자 확대 → 시추/채굴 장비 수요 증가",
                "risks": "유가 급락(OPEC 증산, 수요 둔화) → E&P 투자 축소"
            },
            "Power Boiler & Heat Exchanger": {
                "id": "PCU332410332410",
                "kr_stocks": "두산에너빌리티, BHI",
                "drivers": "발전소 신규 건설 + 기존 설비 교체 수요 → 보일러/열교환기 가격 상승",
                "risks": "석탄발전 퇴출 가속화, 신규 발전소 인허가 지연"
            },
        }
    },
    "Metals & Materials": {
        "series": {
            "Iron & Steel Mills": {
                "id": "PCU331110331110",
                "kr_stocks": "포스코홀딩스, 현대제철, 동국제강",
                "drivers": "인프라 투자 확대 + 철광석 가격 상승 → 철강 제품 가격 인상",
                "risks": "중국 철강 과잉 생산 → 수출 덤핑 → 글로벌 철강 가격 하락"
            },
            "Steel Wire Drawing": {
                "id": "PCU331222331222",
                "kr_stocks": "고려제강, 홍국에너지",
                "drivers": "건설/인프라 수요 → 선재/와이어 수요 증가",
                "risks": "건설경기 침체, 중국산 저가 수입 증가"
            },
            "Aluminum Sheet & Plate": {
                "id": "PCU331315331315",
                "kr_stocks": "노벨리스코리아, 조일알미늄",
                "drivers": "EV 경량화 트렌드 → 자동차용 알루미늄 판재 수요 증가 + 알루미늄 원자재 가격 상승",
                "risks": "EV 판매 둔화, 알루미늄 원자재 가격 급락, 대체소재(탄소섬유) 채용 확대"
            },
            "Copper Rolling & Drawing": {
                "id": "PCU331420331420",
                "kr_stocks": "LS, 풍산",
                "drivers": "전력 인프라/EV/데이터센터 → 구리 수요 폭증 → 구리 가격 사상 최고 근접",
                "risks": "글로벌 경기 침체 → 구리 수요 감소, 광산 증산 → 공급 과잉"
            },
        }
    },
    "Chemical & Materials": {
        "series": {
            "Petrochemical Manufacturing": {
                "id": "PCU325110325110",
                "kr_stocks": "LG화학, 롯데케미칼, 한화솔루션, 금호석유",
                "drivers": "유가 상승 → 납사 가격 상승 → 석유화학 제품 원가 전가",
                "risks": "중국 석화 증설 러시 → 공급 과잉 → 스프레드 축소, 유가 급락"
            },
            "Plastic Material & Resin": {
                "id": "PCU325211325211",
                "kr_stocks": "LG화학, 롯데케미칼, 한화솔루션",
                "drivers": "원자재(에틸렌/프로필렌) 가격 상승 → 수지 제품 가격 인상",
                "risks": "중국 자급률 확대 → 아시아 수급 악화, 재활용 플라스틱 대체 확대"
            },
            "Industrial Gas Mfg": {
                "id": "PCU325120325120",
                "kr_stocks": "SK머티리얼즈, 후성",
                "drivers": "반도체 팹 증설 → 특수가스 수요 급증 → 장기 공급계약 단가 인상",
                "risks": "반도체 다운사이클 → 팹 가동률 하락 → 가스 수요 감소"
            },
            "Paint & Coating Mfg": {
                "id": "PCU325510325510",
                "kr_stocks": "KCC, 삼화페인트, 노루페인트",
                "drivers": "원자재(TiO2, 용제) 가격 상승 + 건설/조선 도료 수요 증가",
                "risks": "건설경기 침체 → 도료 수요 감소, 원자재 가격 하락 시 단가 인하 압력"
            },
        }
    },
    "Construction & Infrastructure": {
        "series": {
            "Construction Machinery Mfg": {
                "id": "PCU333120333120",
                "kr_stocks": "HD현대건설기계, 두산밥캣, 현대건설",
                "drivers": "미국 인프라법/IRA → 건설 프로젝트 증가 → 굴삭기/로더 수요 확대",
                "risks": "금리 인상 → 건설 투자 위축, 중국 건설기계 저가 수출 확대"
            },
            "Concrete Product Mfg": {
                "id": "PCU327390327390",
                "kr_stocks": "삼표시멘트, 한일시멘트, 성신양회",
                "drivers": "인프라/주택 건설 수요 + 시멘트 원가(에너지비) 상승 → 제품 가격 인상",
                "risks": "부동산 침체 → 건설 물량 감소, 탄소배출 규제 → 생산비용 증가"
            },
            "Ready-Mix Concrete": {
                "id": "PCU327320327320",
                "kr_stocks": "유진기업, 삼표시멘트",
                "drivers": "건설 현장 수요 증가 + 원자재(시멘트/골재) 가격 상승 → 레미콘 단가 인상",
                "risks": "주택 착공 감소 → 레미콘 수요 급감, 업체 간 가격 경쟁"
            },
            "Structural Steel Mfg": {
                "id": "PCU332312332312",
                "kr_stocks": "현대스틸산업, 동국S&C",
                "drivers": "데이터센터/물류센터 건설 붐 → 구조용 강재 수요 증가",
                "risks": "상업용 부동산 침체, 철강 가격 하락 → 수익성 악화"
            },
        }
    },
    "Aerospace & Defense": {
        "series": {
            "Aircraft Manufacturing": {
                "id": "PCU336411336411",
                "kr_stocks": "한국항공우주, 한화에어로스페이스",
                "drivers": "항공 여객 회복 → 항공기 신규 주문 급증 → 보잉/에어버스 백로그 사상 최대",
                "risks": "경기 침체 → 항공사 주문 취소/연기, 공급망 병목 해소 시 가격 안정화"
            },
            "Aircraft Engine & Parts": {
                "id": "PCU336412336412",
                "kr_stocks": "한화에어로스페이스, 한국항공우주",
                "drivers": "항공기 인도 확대 + MRO(정비) 수요 폭증 → 엔진/부품 단가 인상",
                "risks": "항공기 인도 지연 장기화, 차세대 엔진 전환 시 구형 부품 수요 감소"
            },
            "Guided Missile & Space Vehicle": {
                "id": "PCU336414336414",
                "kr_stocks": "LIG넥스원, 한화에어로스페이스",
                "drivers": "지정학 긴장 → 각국 국방비 증액 → 미사일/우주 장비 발주 증가",
                "risks": "지정학 긴장 완화 → 국방 예산 축소, 평화 협상 진전"
            },
        }
    },
    "Battery & Storage": {
        "series": {
            "Storage Battery Mfg": {
                "id": "PCU335911335911",
                "kr_stocks": "LG에너지솔루션, 삼성SDI, SK이노베이션",
                "drivers": "EV 판매 확대 + ESS 수요 증가 → 배터리셀 수요 증가 + 리튬/니켈 원자재 가격 반등",
                "risks": "EV 보조금 축소 → 수요 둔화, 중국 CATL 저가 공세, LFP 전환 가속"
            },
            "Primary Battery Mfg": {
                "id": "PCU335912335912",
                "kr_stocks": "LG에너지솔루션, 삼성SDI",
                "drivers": "IoT/의료기기 수요 → 1차전지 안정적 수요 + 원자재 가격 상승",
                "risks": "충전식 배터리로 대체 가속, 원자재 가격 하락"
            },
        }
    },
    "Heavy Machinery": {
        "series": {
            "Industrial Machinery Mfg": {
                "id": "PCU333249333249",
                "kr_stocks": "두산밥캣, HD현대건설기계",
                "drivers": "제조업 리쇼어링 → 공장 신설 → 산업기계 설비투자 확대",
                "risks": "제조업 PMI 하락 → 설비투자 축소, 자동화 전환으로 범용 기계 수요 감소"
            },
            "Pump & Compressor Mfg": {
                "id": "PCU333911333911",
                "kr_stocks": "현대중공업, 한화파워시스템",
                "drivers": "석유화학/발전 플랜트 신규 투자 → 펌프/압축기 수요 증가",
                "risks": "플랜트 투자 사이클 하강, 에너지 전환으로 화석연료 설비 수요 감소"
            },
            "Welding & Soldering Equipment": {
                "id": "PCU333992333992",
                "kr_stocks": "현대종합금속, 세아특수강",
                "drivers": "조선/건설/인프라 수요 → 용접 소재/장비 수요 증가",
                "risks": "조선 수주 감소, 건설경기 침체 → 용접 수요 위축"
            },
        }
    },
    "Telecom & Communication Equipment": {
        "series": {
            "Telephone Apparatus Mfg": {
                "id": "PCU334210334210",
                "kr_stocks": "삼성전자, LG전자",
                "drivers": "AI 스마트폰 교체 사이클 → 단말기 ASP 상승",
                "risks": "스마트폰 시장 포화, 교체 주기 장기화 → 출하량 정체"
            },
            "Radio & TV Broadcasting Equipment": {
                "id": "PCU334220334220",
                "kr_stocks": "삼성전자, LG전자, 이노와이어리스",
                "drivers": "5G 투자 지속 + 방송장비 디지털 전환 → 통신장비 수요 유지",
                "risks": "5G 투자 사이클 종료, 통신사 CAPEX 축소"
            },
        }
    },
    "Automotive & Transportation Equipment": {
        "series": {
            "Automobile Manufacturing": {
                "id": "PCU336111336111",
                "kr_stocks": "현대자동차, 기아, GM코리아",
                "drivers": "EV/하이브리드 전환 → 차량 ASP 상승 + 관세 효과 → 완성차 가격 인상",
                "risks": "경기 침체 → 자동차 수요 감소, EV 가격 전쟁(테슬라/중국), 관세 철회"
            },
            "Motor Vehicle Parts Mfg": {
                "id": "PCU336390336390",
                "kr_stocks": "현대모비스, 만도, HL만도",
                "drivers": "전장화/ADAS 부품 비중 확대 → 부품 단가 상승",
                "risks": "완성차 판매 부진 → OEM 단가 인하 압력, 중국 부품 가격 경쟁"
            },
            "Truck Trailer Mfg": {
                "id": "PCU336212336212",
                "kr_stocks": "현대자동차, 타타대우",
                "drivers": "물류 수요 증가 + 노후차 교체 → 상용차 수요 확대",
                "risks": "화물 운송량 감소, 경기 둔화 → 상용차 수요 위축"
            },
        }
    },
    "Pharmaceutical & Healthcare": {
        "series": {
            "Pharmaceutical Preparation Mfg": {
                "id": "PCU325412325412",
                "kr_stocks": "삼성바이오, 셀트리온, 유한양행, SK바이오팜",
                "drivers": "GLP-1/바이오시밀러 수요 폭증 → CDMO 가동률 상승 → 의약품 단가 인상",
                "risks": "약가 인하 정책(미국 IRA 약가 협상), 바이오시밀러 경쟁 심화"
            },
            "Surgical & Medical Instrument": {
                "id": "PCU339112339112",
                "kr_stocks": "메디톡스, 인터로조, 오스템임플란트",
                "drivers": "고령화 → 수술 건수 증가 → 의료기기 수요 확대 + 원자재 가격 상승",
                "risks": "의료비 억제 정책, 중국산 저가 의료기기 유입"
            },
            "Electromedical Equipment Mfg": {
                "id": "PCU334510334510",
                "kr_stocks": "뷰웍스, 바텍, 인피니트헬스케어",
                "drivers": "AI 의료영상/디지털 헬스케어 투자 확대 → 전자의료장비 수요 증가",
                "risks": "병원 CAPEX 축소, 규제 강화로 신제품 출시 지연"
            },
        }
    },
    "Food & Beverage": {
        "series": {
            "Flour Milling": {
                "id": "PCU311211311211",
                "kr_stocks": "CJ제일제당, 대한제분, 동아원",
                "drivers": "밀 가격 상승(기후/지정학) → 제분 원가 상승 → 밀가루 제품 가격 인상",
                "risks": "밀 풍작/수출국 공급 정상화 → 밀 가격 하락 → 제품 가격 인하 압력"
            },
            "Soybean & Oilseed Processing": {
                "id": "PCU311224311224",
                "kr_stocks": "CJ제일제당, 사조해표",
                "drivers": "대두 가격 상승 + 식용유/사료 수요 증가 → 가공 마진 확대",
                "risks": "남미 대두 풍작 → 대두 가격 급락, 대체 식물성 오일 확대"
            },
            "Soft Drink Mfg": {
                "id": "PCU312111312111",
                "kr_stocks": "롯데칠성, 코카콜라음료",
                "drivers": "설탕/알루미늄캔 원자재 가격 상승 → 음료 제품 가격 인상",
                "risks": "소비 심리 악화 → 수요 감소, 설탕세/건강 규제 강화"
            },
        }
    },
    "Lumber, Paper & Packaging": {
        "series": {
            "Sawmill & Wood Preservation": {
                "id": "PCU321113321113",
                "kr_stocks": "이건산업, 동화기업",
                "drivers": "주택 건설 수요 회복 → 목재 수요 증가 + 산림 벌채 규제 → 공급 제한",
                "risks": "주택 착공 감소(금리 인상), 목재 대체재(철골) 사용 확대"
            },
            "Paper Mills": {
                "id": "PCU322121322121",
                "kr_stocks": "한솔제지, 무림페이퍼",
                "drivers": "펄프 가격 상승 + 포장재 수요 증가 → 제지 제품 가격 인상",
                "risks": "디지털 전환 → 인쇄용지 수요 감소, 재생펄프 확대 → 원가 하락"
            },
            "Corrugated Box Mfg": {
                "id": "PCU322211322211",
                "kr_stocks": "태림포장, 신대양제지",
                "drivers": "이커머스 성장 → 택배 포장 수요 지속 증가 → 골판지 가격 인상",
                "risks": "경기 침체 → 소비 감소 → 포장재 수요 위축, 재활용 원지 가격 변동"
            },
        }
    },
    "Rubber & Plastics": {
        "series": {
            "Tire Manufacturing": {
                "id": "PCU326211326211",
                "kr_stocks": "한국타이어, 넥센타이어, 금호타이어",
                "drivers": "천연고무/합성고무 가격 상승 + 차량 등록대수 증가 → 교체용 타이어 수요 확대",
                "risks": "원자재 가격 급락 시 단가 인하 압력, 중국 타이어 저가 수출 확대"
            },
            "Rubber Product Mfg": {
                "id": "PCU326290326290",
                "kr_stocks": "한국타이어, 평화산업",
                "drivers": "자동차/산업용 고무 부품 수요 증가 + 원자재 가격 상승",
                "risks": "자동차 생산 감소 → 고무 부품 수요 위축, 합성 대체재 확대"
            },
        }
    },
    "Transportation & Logistics": {
        "series": {
            "Railroad Rolling Stock Mfg": {
                "id": "PCU336510336510",
                "kr_stocks": "현대로템, 우진산전",
                "drivers": "각국 철도 투자 확대(탄소중립) → 전동차/철도차량 수주 증가",
                "risks": "정부 예산 삭감, 철도 프로젝트 지연/취소"
            },
            "Ship Building & Repairing": {
                "id": "PCU336611336611",
                "kr_stocks": "HD한국조선해양, 삼성중공업, 한화오션",
                "drivers": "노후 선박 교체 + LNG/암모니아 추진선 수요 → 조선 수주 호황 → 선가 상승",
                "risks": "해운 운임 급락 → 선주 발주 연기, 중국 조선소 저가 수주 공세"
            },
        }
    },
    "Shipbuilding & Marine": {
        "series": {
            "Boat Building": {
                "id": "PCU336612336612",
                "kr_stocks": "HD한국조선해양, 삼성중공업, 한화오션",
                "drivers": "해양 레저/특수선 수요 증가 + 원자재(후판) 가격 상승",
                "risks": "경기 침체 → 레저 보트 수요 감소, 후판 가격 하락"
            },
        }
    },
    "Software & Data Services": {
        "series": {
            "Software Publishers": {
                "id": "PCU511210511210",
                "kr_stocks": "삼성SDS, 카카오, 네이버",
                "drivers": "AI/클라우드 전환 → SaaS 구독료 인상 + 기업 SW 지출 증가",
                "risks": "기업 IT 예산 삭감, 오픈소스 대체 확산, AI로 개발비용 하락"
            },
            "Data Processing & Hosting": {
                "id": "PCU518210518210",
                "kr_stocks": "삼성SDS, NHN, 카카오",
                "drivers": "AI 워크로드 폭증 → 클라우드/데이터센터 호스팅 수요 급증 → 서비스 단가 인상",
                "risks": "빅테크 자체 인프라 확대 → 외부 호스팅 수요 감소, 가격 경쟁 심화"
            },
        }
    },
    "Agriculture & Fertilizer": {
        "series": {
            "Fertilizer Manufacturing": {
                "id": "PCU325311325311",
                "kr_stocks": "남해화학, KG케미칼",
                "drivers": "이란 전쟁 → 천연가스 공급 불안 → 암모니아 가격 급등 → 비료 원가 상승",
                "risks": "이란 종전/휴전 → 천연가스 공급 정상화 → 암모니아/비료 가격 급락"
            },
            "Pesticide Manufacturing": {
                "id": "PCU325320325320",
                "kr_stocks": "경농, 팜한농",
                "drivers": "식량안보 강화 → 농약 사용량 증가 + 원자재(화학물질) 가격 상승",
                "risks": "친환경 농업 규제 강화 → 화학 농약 사용 제한, 바이오 농약 대체"
            },
        }
    },
}

STOCK_CODES = {
    "삼성전자": "005930",
    "SK하이닉스": "000660",
    "DB하이텍": "000990",
    "리노공업": "058470",
    "삼성전기": "009150",
    "LG이노텍": "011070",
    "대덕전자": "353200",
    "심텍": "222800",
    "ISC": "095340",
    "이수페타시스": "007660",
    "비에이치": "090460",
    "LS ELECTRIC": "010120",
    "HD현대일렉트릭": "267260",
    "일진전기": "103590",
    "제룡전기": "033100",
    "현대일렉트릭": "267260",
    "효성중공업": "298040",
    "두산에너빌리티": "034020",
    "한화파워시스템": "456080",
    "TKC": "445180",
    "BHI": "083650",
    "포스코홀딩스": "005490",
    "현대제철": "004020",
    "동국제강": "001230",
    "고려제강": "002240",
    "홍국에너지": "023430",
    "노벨리스코리아": "000560",
    "조일알미늄": "018470",
    "LS": "006260",
    "풍산": "103140",
    "LG화학": "051910",
    "롯데케미칼": "011170",
    "한화솔루션": "009830",
    "금호석유": "011780",
    "SK머티리얼즈": "036490",
    "후성": "093370",
    "KCC": "002380",
    "삼화페인트": "000390",
    "노루페인트": "090350",
    "HD현대건설기계": "267270",
    "두산밥캣": "241560",
    "현대건설": "000720",
    "삼표시멘트": "038500",
    "한일시멘트": "300720",
    "성신양회": "004980",
    "유진기업": "023410",
    "현대스틸산업": "071090",
    "동국S&C": "100130",
    "한국항공우주": "047810",
    "한화에어로스페이스": "012450",
    "LIG넥스원": "079550",
    "LG에너지솔루션": "373220",
    "삼성SDI": "006400",
    "SK이노베이션": "096770",
    "현대중공업": "329180",
    "현대종합금속": "010420",
    "세아특수강": "019440",
    "LG전자": "066570",
    "이노와이어리스": "073490",
    "현대자동차": "005380",
    "기아": "000270",
    "현대모비스": "012330",
    "만도": "204320",
    "HL만도": "204320",
    "삼성바이오": "207940",
    "셀트리온": "068270",
    "유한양행": "000100",
    "SK바이오팜": "326030",
    "메디톡스": "086900",
    "인터로조": "119610",
    "오스템임플란트": "048260",
    "뷰웍스": "100120",
    "바텍": "043150",
    "인피니트헬스케어": "071200",
    "CJ제일제당": "097950",
    "대한제분": "001130",
    "동아원": "088910",
    "사조해표": "003230",
    "롯데칠성": "005300",
    "코카콜라음료": "017180",
    "이건산업": "008250",
    "동화기업": "025900",
    "한솔제지": "213500",
    "무림페이퍼": "009580",
    "태림포장": "011280",
    "신대양제지": "016590",
    "한국타이어": "161390",
    "넥센타이어": "002350",
    "금호타이어": "073240",
    "평화산업": "090080",
    "현대로템": "064350",
    "우진산전": "091580",
    "HD한국조선해양": "009540",
    "삼성중공업": "010140",
    "한화오션": "042660",
    "삼성SDS": "018260",
    "카카오": "035720",
    "네이버": "035420",
    "NHN": "181710",
    "남해화학": "025860",
    "KG케미칼": "001390",
    "경농": "002100",
    "팜한농": "036580",
    "GM코리아": "013000",
    "타타대우": "004100",
}

SIGNAL_COLORS = {
    "Strong Uptrend": "#ff4444",
    "Moderate Uptrend": "#ff8c00",
    "Reversal": "#ffaa00",
    "Momentum": "#00cc66",
    "Cooling After Rise": "#888888",
    "Flat": "#666666",
    "Mild Decline": "#cc44ff",
    "Deep Decline": "#ff0066",
}

SIGNAL_LABELS_KR = {
    "Strong Uptrend": "강한 상승",
    "Moderate Uptrend": "완만한 상승",
    "Reversal": "반전",
    "Momentum": "모멘텀",
    "Cooling After Rise": "상승 후 냉각",
    "Flat": "보합",
    "Mild Decline": "완만한 하락",
    "Deep Decline": "급락",
}
