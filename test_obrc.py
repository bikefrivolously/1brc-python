import obrc


def test_answer():
    expected = [
        "Abha=-26.4/18.0/56.3",
        "Abidjan=-14.7/26.0/68.0",
        "Abéché=-10.1/29.5/69.8",
        "Accra=-12.0/26.4/66.4",
        "Addis Ababa=-25.0/16.1/56.0",
        "Adelaide=-22.3/17.3/55.5",
        "Aden=-11.9/29.1/66.2",
        "Ahvaz=-14.3/25.4/64.1",
        "Albuquerque=-24.1/14.0/56.8",
        "Alexandra=-29.3/11.0/54.9",
        "Alexandria=-20.1/20.0/61.4",
        "Algiers=-23.9/18.2/64.5",
        "Alice Springs=-21.2/21.1/60.6",
        "Almaty=-35.2/10.0/47.7",
        "Amsterdam=-30.3/10.2/47.2",
        "Anadyr=-48.7/-6.8/35.1",
        "Anchorage=-33.8/2.8/43.3",
        "Andorra la Vella=-27.8/9.8/49.4",
        "Ankara=-29.2/11.9/51.6",
        "Antananarivo=-26.4/17.9/60.0",
        "Antsiranana=-13.4/25.1/65.7",
        "Arkhangelsk=-38.0/1.2/44.4",
        "Ashgabat=-21.6/17.2/55.8",
        "Asmara=-24.8/15.6/51.0",
        "Assab=-11.6/30.5/70.4",
        "Astana=-36.5/3.6/43.6",
        "Athens=-19.4/19.1/58.8",
        "Atlanta=-21.4/17.1/61.7",
        "Auckland=-26.3/15.2/55.1",
        "Austin=-17.0/20.7/58.9",
        "Baghdad=-14.7/22.7/62.0",
        "Baguio=-23.4/19.5/59.1",
        "Baku=-28.2/15.2/54.9",
        "Baltimore=-26.0/13.0/54.3",
        "Bamako=-11.3/27.9/69.3",
        "Bangkok=-9.2/28.7/66.9",
        "Bangui=-10.4/26.0/64.8",
        "Banjul=-12.1/25.9/66.4",
        "Barcelona=-24.3/18.3/62.3",
        "Bata=-13.5/25.2/63.6",
        "Batumi=-26.4/14.1/62.9",
        "Beijing=-25.0/12.8/49.1",
        "Beirut=-26.4/20.9/59.6",
        "Belgrade=-30.4/12.5/48.4",
        "Belize City=-16.3/26.6/63.1",
        "Benghazi=-18.9/19.9/58.3",
        "Bergen=-36.0/7.7/45.7",
        "Berlin=-29.6/10.4/49.4",
        "Bilbao=-23.2/14.6/59.4",
        "Birao=-16.2/26.5/69.3",
        "Bishkek=-27.0/11.4/50.1",
        "Bissau=-15.6/27.0/68.4",
        "Blantyre=-20.8/22.1/62.1",
        "Bloemfontein=-22.6/15.7/57.3",
        "Boise=-28.6/11.5/53.6",
        "Bordeaux=-26.0/14.3/55.5",
        "Bosaso=-18.7/30.1/71.3",
        "Boston=-29.2/11.0/50.6",
        "Bouaké=-9.8/26.0/65.1",
        "Bratislava=-32.1/10.5/51.5",
        "Brazzaville=-12.0/25.1/70.9",
        "Bridgetown=-14.3/27.0/65.9",
        "Brisbane=-19.8/21.4/65.8",
        "Brussels=-30.6/10.5/55.0",
        "Bucharest=-29.9/10.9/47.0",
        "Budapest=-26.0/11.2/47.7",
        "Bujumbura=-13.1/23.8/65.2",
        "Bulawayo=-25.8/18.9/56.7",
        "Burnie=-27.3/13.0/50.5",
        "Busan=-29.2/15.0/63.3",
        "Cabo San Lucas=-14.8/24.0/64.8",
        "Cairns=-17.0/25.0/67.5",
        "Cairo=-16.7/21.4/63.1",
        "Calgary=-39.4/4.4/49.6",
        "Canberra=-23.4/13.1/54.2",
        "Cape Town=-28.9/16.2/57.9",
        "Changsha=-23.6/17.4/53.1",
        "Charlotte=-27.0/16.3/59.7",
        "Chiang Mai=-13.6/25.8/68.0",
        "Chicago=-28.1/9.8/49.2",
        "Chihuahua=-24.9/18.6/57.4",
        "Chittagong=-20.0/25.9/67.6",
        "Chișinău=-26.1/10.1/46.9",
        "Chongqing=-20.7/18.6/66.6",
        "Christchurch=-26.4/12.2/50.8",
        "City of San Marino=-35.0/11.9/50.1",
        "Colombo=-15.3/27.5/64.2",
        "Columbus=-36.9/11.7/51.7",
        "Conakry=-14.5/26.4/66.2",
        "Copenhagen=-29.6/9.2/52.0",
        "Cotonou=-15.2/27.2/73.7",
        "Cracow=-32.0/9.3/46.8",
        "Da Lat=-19.9/17.9/57.9",
        "Da Nang=-10.9/25.8/67.8",
        "Dakar=-12.8/24.0/65.6",
        "Dallas=-25.2/18.9/62.1",
        "Damascus=-23.6/17.0/59.1",
        "Dampier=-12.5/26.5/64.6",
        "Dar es Salaam=-14.5/25.8/73.3",
        "Darwin=-13.1/27.6/65.2",
        "Denpasar=-17.2/23.7/62.1",
        "Denver=-28.1/10.4/50.1",
        "Detroit=-31.8/10.1/48.9",
        "Dhaka=-12.1/25.9/65.9",
        "Dikson=-49.4/-11.1/31.2",
        "Dili=-10.7/26.7/68.1",
        "Djibouti=-8.7/29.8/76.0",
        "Dodoma=-19.6/22.7/66.1",
        "Dolisie=-16.0/24.0/65.6",
        "Douala=-17.8/26.7/66.2",
        "Dubai=-15.2/27.0/68.2",
        "Dublin=-31.3/9.8/50.0",
        "Dunedin=-28.3/11.1/49.3",
        "Durban=-15.4/20.6/59.9",
        "Dushanbe=-24.7/14.8/52.9",
        "Edinburgh=-30.8/9.3/52.7",
        "Edmonton=-34.2/4.2/45.5",
        "El Paso=-19.9/18.0/60.6",
        "Entebbe=-17.2/21.0/61.8",
        "Erbil=-21.4/19.6/59.9",
        "Erzurum=-37.7/5.1/43.8",
        "Fairbanks=-42.7/-2.2/36.4",
        "Fianarantsoa=-19.9/17.9/58.1",
        "Flores,  Petén=-11.4/26.5/63.9",
        "Frankfurt=-28.3/10.6/51.6",
        "Fresno=-23.7/17.9/58.5",
        "Fukuoka=-23.5/17.1/55.2",
        "Gaborone=-16.7/21.1/60.4",
        "Gabès=-20.2/19.4/57.6",
        "Gagnoa=-14.9/26.0/69.8",
        "Gangtok=-25.7/15.2/53.4",
        "Garissa=-5.3/29.3/68.5",
        "Garoua=-15.2/28.3/70.9",
        "George Town=-12.8/27.9/69.3",
        "Ghanzi=-21.7/21.5/59.2",
        "Gjoa Haven=-53.3/-14.4/25.5",
        "Guadalajara=-16.8/20.8/62.8",
        "Guangzhou=-22.5/22.4/64.1",
        "Guatemala City=-15.4/20.3/59.6",
        "Halifax=-32.3/7.5/50.4",
        "Hamburg=-29.1/9.8/45.7",
        "Hamilton=-35.8/13.8/56.7",
        "Hanga Roa=-31.7/20.5/59.2",
        "Hanoi=-16.2/23.6/62.9",
        "Harare=-21.3/18.3/57.4",
        "Harbin=-35.6/5.0/44.5",
        "Hargeisa=-15.3/21.6/67.1",
        "Hat Yai=-13.6/27.0/68.6",
        "Havana=-13.9/25.2/63.5",
        "Helsinki=-36.0/5.9/48.6",
        "Heraklion=-23.6/18.9/70.1",
        "Hiroshima=-24.9/16.3/57.6",
        "Ho Chi Minh City=-10.8/27.4/63.8",
        "Hobart=-27.2/12.6/53.6",
        "Hong Kong=-17.6/23.4/66.6",
        "Honiara=-12.7/26.6/66.4",
        "Honolulu=-17.8/25.4/64.6",
        "Houston=-17.9/20.7/59.7",
        "Ifrane=-32.1/11.4/51.3",
        "Indianapolis=-25.8/11.8/50.6",
        "Iqaluit=-52.0/-9.3/37.2",
        "Irkutsk=-42.3/0.9/41.0",
        "Istanbul=-22.3/13.9/56.3",
        "Jacksonville=-16.8/20.3/68.0",
        "Jakarta=-10.6/26.7/68.5",
        "Jayapura=-11.2/26.9/69.2",
        "Jerusalem=-27.1/18.3/59.4",
        "Johannesburg=-22.8/15.5/52.2",
        "Jos=-19.0/22.8/60.3",
        "Juba=-12.3/27.9/68.9",
        "Kabul=-26.7/12.1/53.1",
        "Kampala=-15.5/20.0/59.7",
        "Kandi=-12.4/27.8/68.5",
        "Kankan=-15.2/26.4/63.7",
        "Kano=-19.1/26.3/64.1",
        "Kansas City=-28.1/12.5/50.3",
        "Karachi=-16.9/26.0/65.5",
        "Karonga=-19.1/24.5/69.3",
        "Kathmandu=-30.3/18.3/62.6",
        "Khartoum=-11.6/29.9/69.6",
        "Kingston=-10.2/27.4/66.7",
        "Kinshasa=-15.3/25.3/70.1",
        "Kolkata=-13.5/26.7/67.6",
        "Kuala Lumpur=-15.9/27.3/71.8",
        "Kumasi=-15.8/26.0/67.4",
        "Kunming=-25.2/15.6/55.6",
        "Kuopio=-34.6/3.4/55.5",
        "Kuwait City=-13.1/25.8/64.1",
        "Kyiv=-33.9/8.4/47.7",
        "Kyoto=-24.3/15.7/60.2",
        "La Ceiba=-13.1/26.2/68.9",
        "La Paz=-25.3/23.7/63.0",
        "Lagos=-12.5/26.8/68.2",
        "Lahore=-12.2/24.4/69.0",
        "Lake Havasu City=-17.7/23.7/61.4",
        "Lake Tekapo=-31.8/8.7/49.3",
        "Las Palmas de Gran Canaria=-19.2/21.3/69.8",
        "Las Vegas=-20.4/20.2/58.3",
        "Launceston=-28.2/13.0/55.0",
        "Lhasa=-30.7/7.6/46.9",
        "Libreville=-19.2/26.0/63.8",
        "Lisbon=-20.5/17.4/62.5",
        "Livingstone=-17.8/21.7/64.2",
        "Ljubljana=-32.0/10.9/49.6",
        "Lodwar=-13.1/29.3/67.3",
        "Lomé=-14.7/27.0/64.6",
        "London=-38.9/11.3/50.4",
        "Los Angeles=-20.2/18.6/58.1",
        "Louisville=-28.2/13.7/56.4",
        "Luanda=-14.6/25.9/66.2",
        "Lubumbashi=-19.8/20.7/62.3",
        "Lusaka=-23.7/19.9/60.9",
        "Luxembourg City=-32.7/9.3/50.5",
        "Lviv=-29.5/7.8/47.5",
        "Lyon=-25.3/12.5/54.5",
        "Madrid=-24.0/15.0/50.6",
        "Mahajanga=-16.6/26.4/68.9",
        "Makassar=-12.6/26.7/68.3",
        "Makurdi=-14.3/26.0/66.0",
        "Malabo=-12.4/26.3/69.2",
        "Malé=-11.2/28.0/67.2",
        "Managua=-9.8/27.4/70.8",
        "Manama=-11.1/26.4/65.3",
        "Mandalay=-8.4/27.9/66.5",
        "Mango=-11.1/28.1/72.5",
        "Manila=-11.2/28.5/66.8",
        "Maputo=-16.6/22.8/61.6",
        "Marrakesh=-22.6/19.6/61.3",
        "Marseille=-25.8/15.7/52.2",
        "Maun=-15.9/22.3/61.3",
        "Medan=-14.7/26.4/64.0",
        "Mek'ele=-19.5/22.7/65.4",
        "Melbourne=-24.2/15.2/58.4",
        "Memphis=-26.3/17.3/56.7",
        "Mexicali=-20.9/23.1/65.0",
        "Mexico City=-23.1/17.5/59.8",
        "Miami=-16.3/24.9/63.3",
        "Milan=-28.7/13.0/51.1",
        "Milwaukee=-40.4/9.0/48.6",
        "Minneapolis=-33.8/7.8/45.5",
        "Minsk=-32.3/6.7/47.6",
        "Mogadishu=-10.4/27.1/66.0",
        "Mombasa=-13.7/26.2/64.7",
        "Monaco=-23.6/16.5/58.8",
        "Moncton=-36.8/6.2/47.4",
        "Monterrey=-17.0/22.3/70.2",
        "Montreal=-31.4/6.7/49.1",
        "Moscow=-32.2/5.8/44.6",
        "Mumbai=-14.9/27.2/64.0",
        "Murmansk=-37.5/0.7/44.4",
        "Muscat=-11.1/27.9/66.1",
        "Mzuzu=-23.9/17.6/63.3",
        "N'Djamena=-11.8/28.3/71.3",
        "Naha=-15.3/23.3/64.0",
        "Nairobi=-22.5/17.9/57.6",
        "Nakhon Ratchasima=-16.4/27.3/68.3",
        "Napier=-25.1/14.6/56.1",
        "Napoli=-22.4/15.9/55.0",
        "Nashville=-26.1/15.4/59.6",
        "Nassau=-17.1/24.5/64.0",
        "Ndola=-19.8/20.3/56.8",
        "New Delhi=-13.1/24.9/63.0",
        "New Orleans=-15.9/20.7/56.5",
        "New York City=-30.0/12.9/54.8",
        "Ngaoundéré=-16.1/22.1/59.4",
        "Niamey=-9.7/29.4/67.3",
        "Nicosia=-19.7/19.7/61.7",
        "Niigata=-22.0/13.8/52.2",
        "Nouadhibou=-16.8/21.3/60.0",
        "Nouakchott=-12.1/25.6/64.6",
        "Novosibirsk=-38.7/1.5/40.5",
        "Nuuk=-43.8/-1.3/36.9",
        "Odesa=-39.6/10.6/52.8",
        "Odienné=-11.4/25.9/62.2",
        "Oklahoma City=-27.5/16.0/54.5",
        "Omaha=-29.0/10.6/48.0",
        "Oranjestad=-13.6/28.1/69.0",
        "Oslo=-33.5/5.6/46.6",
        "Ottawa=-32.8/6.5/52.3",
        "Ouagadougou=-8.5/28.4/70.6",
        "Ouahigouya=-10.3/28.5/65.2",
        "Ouarzazate=-20.3/19.0/53.5",
        "Oulu=-41.0/2.7/42.9",
        "Palembang=-17.4/27.2/66.9",
        "Palermo=-20.0/18.5/61.6",
        "Palm Springs=-12.9/24.4/65.7",
        "Palmerston North=-25.4/13.2/55.1",
        "Panama City=-12.4/28.0/73.9",
        "Parakou=-11.2/26.7/68.0",
        "Paris=-25.5/12.2/54.2",
        "Perth=-27.7/18.7/58.5",
        "Petropavlovsk-Kamchatsky=-35.7/1.8/41.1",
        "Philadelphia=-29.7/13.1/53.5",
        "Phnom Penh=-10.0/28.4/76.8",
        "Phoenix=-17.4/23.9/65.9",
        "Pittsburgh=-29.7/10.8/55.4",
        "Podgorica=-21.5/15.3/56.1",
        "Pointe-Noire=-23.2/26.1/63.3",
        "Pontianak=-9.1/27.7/65.9",
        "Port Moresby=-9.7/26.9/75.1",
        "Port Sudan=-11.2/28.3/64.1",
        "Port Vila=-15.0/24.3/61.1",
        "Port-Gentil=-13.8/26.0/67.3",
        "Portland (OR)=-24.2/12.5/53.5",
        "Porto=-25.1/15.7/53.8",
        "Prague=-34.3/8.4/45.9",
        "Praia=-16.9/24.3/63.4",
        "Pretoria=-21.2/18.2/59.2",
        "Pyongyang=-37.7/10.8/48.5",
        "Rabat=-19.6/17.1/53.7",
        "Rangpur=-11.3/24.4/62.1",
        "Reggane=-9.6/28.3/68.6",
        "Reykjavík=-31.5/4.3/47.5",
        "Riga=-30.5/6.1/46.0",
        "Riyadh=-12.3/26.0/62.8",
        "Rome=-20.7/15.1/53.1",
        "Roseau=-12.5/26.2/66.1",
        "Rostov-on-Don=-30.6/10.0/49.7",
        "Sacramento=-22.5/16.3/59.7",
        "Saint Petersburg=-33.8/5.8/47.3",
        "Saint-Pierre=-34.5/5.7/48.5",
        "Salt Lake City=-26.2/11.7/55.8",
        "San Antonio=-19.8/20.7/62.8",
        "San Diego=-22.9/17.8/59.1",
        "San Francisco=-23.0/14.5/52.5",
        "San Jose=-25.1/16.4/55.2",
        "San José=-17.2/22.6/59.3",
        "San Juan=-18.9/27.2/64.3",
        "San Salvador=-20.2/23.1/67.2",
        "Sana'a=-25.1/20.0/58.0",
        "Santo Domingo=-17.0/25.9/66.0",
        "Sapporo=-29.0/8.8/45.4",
        "Sarajevo=-25.2/10.1/50.0",
        "Saskatoon=-34.4/3.3/43.0",
        "Seattle=-25.9/11.5/53.6",
        "Seoul=-26.6/12.4/52.9",
        "Seville=-19.4/19.2/61.0",
        "Shanghai=-30.1/16.7/51.3",
        "Singapore=-12.7/27.0/62.4",
        "Skopje=-27.9/12.5/54.6",
        "Sochi=-25.2/14.2/53.7",
        "Sofia=-38.5/10.6/49.2",
        "Sokoto=-12.9/28.0/64.4",
        "Split=-23.1/16.2/68.6",
        "St. John's=-35.7/5.0/44.7",
        "St. Louis=-27.4/13.9/59.4",
        "Stockholm=-41.9/6.6/46.5",
        "Surabaya=-10.4/26.9/65.0",
        "Suva=-12.7/25.8/63.5",
        "Suwałki=-32.1/7.2/43.8",
        "Sydney=-21.9/17.7/62.8",
        "Ségou=-10.7/28.1/70.7",
        "Tabora=-16.0/23.1/62.7",
        "Tabriz=-33.6/12.6/52.8",
        "Taipei=-18.9/23.0/61.6",
        "Tallinn=-33.7/6.4/46.2",
        "Tamale=-12.0/27.8/69.5",
        "Tamanrasset=-18.3/21.7/61.4",
        "Tampa=-22.9/22.9/66.7",
        "Tashkent=-25.9/14.8/57.0",
        "Tauranga=-22.2/14.8/53.7",
        "Tbilisi=-28.1/12.9/57.6",
        "Tegucigalpa=-19.5/21.7/62.6",
        "Tehran=-21.0/17.0/60.5",
        "Tel Aviv=-19.2/20.0/58.3",
        "Thessaloniki=-21.3/15.9/57.9",
        "Thiès=-16.6/24.0/63.9",
        "Tijuana=-25.3/17.8/57.7",
        "Timbuktu=-15.2/28.0/76.1",
        "Tirana=-25.4/15.3/53.2",
        "Toamasina=-22.2/23.4/61.3",
        "Tokyo=-23.5/15.3/56.9",
        "Toliara=-17.6/24.0/64.8",
        "Toluca=-29.9/12.4/52.6",
        "Toronto=-31.3/9.5/53.6",
        "Tripoli=-22.9/20.0/59.1",
        "Tromsø=-38.4/2.9/43.2",
        "Tucson=-17.5/21.0/61.2",
        "Tunis=-20.6/18.6/56.9",
        "Ulaanbaatar=-41.1/-0.5/39.0",
        "Upington=-17.9/20.4/61.8",
        "Vaduz=-27.6/10.1/47.2",
        "Valencia=-19.9/18.4/59.3",
        "Valletta=-20.7/18.9/60.6",
        "Vancouver=-25.0/10.4/48.6",
        "Veracruz=-15.5/25.5/66.5",
        "Vienna=-28.1/10.4/53.5",
        "Vientiane=-14.9/25.9/63.7",
        "Villahermosa=-13.3/27.1/68.4",
        "Vilnius=-36.5/6.0/43.8",
        "Virginia Beach=-26.8/15.7/55.5",
        "Vladivostok=-31.1/5.0/50.3",
        "Warsaw=-33.7/8.4/55.1",
        "Washington, D.C.=-27.3/14.6/54.5",
        "Wau=-23.3/27.7/74.6",
        "Wellington=-27.5/12.9/55.9",
        "Whitehorse=-40.1/-0.1/43.5",
        "Wichita=-24.7/13.8/51.4",
        "Willemstad=-12.6/27.9/65.4",
        "Winnipeg=-37.4/3.0/41.5",
        "Wrocław=-29.4/9.6/53.8",
        "Xi'an=-29.5/14.1/58.0",
        "Yakutsk=-50.6/-8.8/34.5",
        "Yangon=-12.8/27.5/69.5",
        "Yaoundé=-14.0/23.9/63.4",
        "Yellowknife=-44.3/-4.2/34.9",
        "Yerevan=-31.5/12.4/55.9",
        "Yinchuan=-30.1/9.0/47.2",
        "Zagreb=-34.6/10.7/50.1",
        "Zanzibar City=-18.2/26.0/68.1",
        "Zürich=-33.8/9.1/47.2",
        "Ürümqi=-35.8/7.5/48.7",
        "İzmir=-20.7/17.9/58.5",
    ]
    answer = obrc.do_calc("../1brc/measurements_small.txt")
    assert answer == expected