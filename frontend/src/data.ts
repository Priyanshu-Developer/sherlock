
function getRandomDate() {
  // Returns a date string between 2025-06-01 and 2025-07-31
  const start = new Date('2025-06-01').getTime();
  const end = new Date('2025-07-31').getTime();
  const randomTime = start + Math.random() * (end - start);
  const date = new Date(randomTime);
  // Format as YYYY-MM-DD
  return date.toISOString().slice(0, 10);
}

export interface Row {
  id: number;
  phoneNo: string;
  status: number;
  date: string;

}



export const initialRows: Row[] = [
  {
    id: 1,
    phoneNo: "919876543210",
    status: 2,
    date: getRandomDate(),
  },
  {
    id: 2,
    phoneNo: "919987654321",
    status: 4,
    date: getRandomDate(),
  },
  {
    id: 3,
    phoneNo: "919765432109",
    status: 1,
    date: getRandomDate(),
  },
  {
    id: 4,
    phoneNo: "919654321098",
    status: 3,
    date: getRandomDate(),
  },
  {
    id: 5,
    phoneNo: "919543210987",
    status: 2,
    date: getRandomDate(),
  },
  {
    id: 6,
    phoneNo: "919432109876",
    status: 4,
    date: getRandomDate(),
  },
  {
    id: 7,
    phoneNo: "919321098765",
    status: 1,
    date: getRandomDate(),
  },
  {
    id: 8,
    phoneNo: "919210987654",
    status: 3,
    date: getRandomDate(),
  },
  {
    id: 9,
    phoneNo: "919109876543",
    status: 2,
    date: getRandomDate(),
  },
  {
    id: 10,
    phoneNo: "919098765432",
    status: 4,
    date: getRandomDate(),
  },
  {
    id: 11,
    phoneNo: "918987654321",
    status: 1,
    date: getRandomDate(),

  },
  {
    id: 12,
    phoneNo: "918876543210",
    status: 3,
    date: getRandomDate(),

  },
  {
    id: 13,
    phoneNo: "918765432109",
    status: 2,
    date: getRandomDate(),

  },
  {
    id: 14,
    phoneNo: "918654321098",
    status: 4,
    date: getRandomDate(),

  },
  {
    id: 15,
    phoneNo: "918543210987",
    status: 1,
    date: getRandomDate()
  },
  {
    id: 16,
    phoneNo: "918432109876",
    status: 3,
    date: getRandomDate()
  },
  {
    id: 17,
    phoneNo: "918321098765",
    status: 2,
    date: getRandomDate()
  },
  {
    id: 18,
    phoneNo: "918210987654",
    status: 4,
    date: getRandomDate()
  },
  {
    id: 19,
    phoneNo: "918109876543",
    status: 1,
    date: getRandomDate()
  },
  {
    id: 20,
    phoneNo: "918098765432",
    status: 3,
    date: getRandomDate()
  },
  {
    id: 21,
    phoneNo: "917987654321",
    status: 2,
    date: getRandomDate()
  },
  {
    id: 22,
    phoneNo: "917876543210",
    status: 4,
    date: getRandomDate()
  },
  {
    id: 23,
    phoneNo: "917765432109",
    status: 1,
    date: getRandomDate()
  },
  {
    id: 24,
    phoneNo: "917654321098",
    status: 3,
    date: getRandomDate()
  },
  {
    id: 25,
    phoneNo: "917543210987",
    status: 2,
    date: getRandomDate()
  },
  {
    id: 26,
    phoneNo: "917432109876",
    status: 4,
    date: getRandomDate()
  },
  {
    id: 27,
    phoneNo: "917321098765",
    status: 1,
    date: getRandomDate()
  },
  {
    id: 28,
    phoneNo: "917210987654",
    status: 3,
    date: getRandomDate()
  },
  {
    id: 29,
    phoneNo: "917109876543",
    status: 2,
    date: getRandomDate()
  },
  {
    id: 30,
    phoneNo: "917098765432",
    status: 4,
    date: getRandomDate()
  },
  {
    id: 31,
    phoneNo: "916987654321",
    status: 1,
    date: getRandomDate()
  },
  {
    id: 32,
    phoneNo: "916876543210",
    status: 3,
    date: getRandomDate()
  },
  {
    id: 33,
    phoneNo: "916765432109",
    status: 2,
    date: getRandomDate()
  },
  {
    id: 34,
    phoneNo: "916654321098",
    status: 4,
    date: getRandomDate()
  },
  {
    id: 35,
    phoneNo: "916543210987",
    status: 1,
    date: getRandomDate()
  },
  {
    id: 36,
    phoneNo: "916432109876",
    status: 3,
    date: getRandomDate()
  },
  {
    id: 37,
    phoneNo: "916321098765",
    status: 2,
    date: getRandomDate()
  },
  {
    id: 38,
    phoneNo: "916210987654",
    status: 4,
    date: getRandomDate()
  },
  {
    id: 39,
    phoneNo: "916109876543",
    status: 1,
    date: getRandomDate()
  },
  {
    id: 40,
    phoneNo: "916098765432",
    status: 3,
    date: getRandomDate()
  },
  {
    id: 41,
    phoneNo: "915987654321",
    status: 2,
    date: getRandomDate()
  },
  {
    id: 42,
    phoneNo: "915876543210",
    status: 4,
    date: getRandomDate()
  },
  {
    id: 43,
    phoneNo: "915765432109",
    status: 1,
    date: getRandomDate()
  },
  {
    id: 44,
    phoneNo: "915654321098",
    status: 3,
    date: getRandomDate()
  },
  {
    id: 45,
    phoneNo: "915543210987",
    status: 2,
    date: getRandomDate()
  },
  {
    id: 46,
    phoneNo: "915432109876",
    status: 4,
    date: getRandomDate()
  },
  {
    id: 47,
    phoneNo: "915321098765",
    status: 1,
    date: getRandomDate()
  },
  {
    id: 48,
    phoneNo: "915210987654",
    status: 3,
    date: getRandomDate()
  },
  {
    id: 49,
    phoneNo: "915109876543",
    status: 2,
    date: getRandomDate()
  },
  {
    id: 50,
    phoneNo: "915098765432",
    status: 4,
    date: getRandomDate()
  },
  {
    id: 51,
    phoneNo: "914987654321",
    status: 1,
    date: getRandomDate()
  },
  {
    id: 52,
    phoneNo: "914876543210",
    status: 3,
    date: getRandomDate()
  },
  {
    id: 53,
    phoneNo: "914765432109",
    status: 2,
    date: getRandomDate()
  },
  {
    id: 54,
    phoneNo: "914654321098",
    status: 4,
    date: getRandomDate()
  },
  {
    id: 55,
    phoneNo: "914543210987",
    status: 1,
    date: getRandomDate()
  },
  {
    id: 56,
    phoneNo: "914432109876",
    status: 3,
    date: getRandomDate()
  },
  {
    id: 57,
    phoneNo: "914321098765",
    status: 2,
    date: getRandomDate()
  },
  {
    id: 58,
    phoneNo: "914210987654",
    status: 4,
    date: getRandomDate()
  },
  {
    id: 59,
    phoneNo: "914109876543",
    status: 1,
    date: getRandomDate()
  },
  {
    id: 60,
    phoneNo: "914098765432",
    status: 3,
    date: getRandomDate()
  },
  {
    id: 61,
    phoneNo: "913987654321",
    status: 2,
    date: getRandomDate()
  },
  {
    id: 62,
    phoneNo: "913876543210",
    status: 4,
    date: getRandomDate()
  },
  {
    id: 63,
    phoneNo: "913765432109",
    status: 1,
    date: getRandomDate()
  },
  {
    id: 64,
    phoneNo: "913654321098",
    status: 3,
    date: getRandomDate()
  },
  {
    id: 65,
    phoneNo: "913543210987",
    status: 2,
    date: getRandomDate()
  },
  {
    id: 66,
    phoneNo: "913432109876",
    status: 4,
    date: getRandomDate()
  },
  {
    id: 67,
    phoneNo: "913321098765",
    status: 1,
    date: getRandomDate()
  },
  {
    id: 68,
    phoneNo: "913210987654",
    status: 3,
    date: getRandomDate()
  },
  {
    id: 69,
    phoneNo: "913109876543",
    status: 2,
    date: getRandomDate()
  },
  {
    id: 70,
    phoneNo: "913098765432",
    status: 4,
    date: getRandomDate()
  },
  {
    id: 71,
    phoneNo: "912987654321",
    status: 1,
    date: getRandomDate()
  },
  {
    id: 72,
    phoneNo: "912876543210",
    status: 3,
    date: getRandomDate()
  },
  {
    id: 73,
    phoneNo: "912765432109",
    status: 2,
    date: getRandomDate()
  },
  {
    id: 74,
    phoneNo: "912654321098",
    status: 4,
    date: getRandomDate()
  },
  {
    id: 75,
    phoneNo: "912543210987",
    status: 1,
    date: getRandomDate()
  },
  {
    id: 76,
    phoneNo: "912432109876",
    status: 3,
    date: getRandomDate()
  },
  {
    id: 77,
    phoneNo: "912321098765",
    status: 2,
    date: getRandomDate()
  },
  {
    id: 78,
    phoneNo: "912210987654",
    status: 4,
    date: getRandomDate()
  },
  {
    id: 79,
    phoneNo: "912109876543",
    status: 1,
    date: getRandomDate()
  },
  {
    id: 80,
    phoneNo: "912098765432",
    status: 3,
    date: getRandomDate()
  },
  {
    id: 81,
    phoneNo: "911987654321",
    status: 2,
    date: getRandomDate()
  },
  {
    id: 82,
    phoneNo: "911876543210",
    status: 4,
    date: getRandomDate()
  },
  {
    id: 83,
    phoneNo: "911765432109",
    status: 1,
    date: getRandomDate()
  },
  {
    id: 84,
    phoneNo: "911654321098",
    status: 3,
    date: getRandomDate()
  },
  {
    id: 85,
    phoneNo: "911543210987",
    status: 2,
    date: getRandomDate()
  },
  {
    id: 86,
    phoneNo: "911432109876",
    status: 4,
    date: getRandomDate()
  },
  {
    id: 87,
    phoneNo: "911321098765",
    status: 1,
    date: getRandomDate()
  },
  {
    id: 88,
    phoneNo: "911210987654",
    status: 3,
    date: getRandomDate()
  },
  {
    id: 89,
    phoneNo: "911109876543",
    status: 2,
    date: getRandomDate()
  },
  {
    id: 90,
    phoneNo: "911098765432",
    status: 4,
    date: getRandomDate()
  },
  {
    id: 91,
    phoneNo: "910987654321",
    status: 1,
    date: getRandomDate()
  },
  {
    id: 92,
    phoneNo: "910876543210",
    status: 3,
    date: getRandomDate()
  },
  {
    id: 93,
    phoneNo: "910765432109",
    status: 2,
    date: getRandomDate()
  },
  {
    id: 94,
    phoneNo: "910654321098",
    status: 4,
    date: getRandomDate()
  },
  {
    id: 95,
    phoneNo: "910543210987",
    status: 1,
    date: getRandomDate()
  },
  {
    id: 96,
    phoneNo: "910432109876",
    status: 3,
    date: getRandomDate()
  },
  {
    id: 97,
    phoneNo: "910321098765",
    status: 2,
    date: getRandomDate()
  },
  {
    id: 98,
    phoneNo: "910210987654",
    status: 4,
    date: getRandomDate()
  },
  {
    id: 99,
    phoneNo: "910109876543",
    status: 1,
    date: getRandomDate()
  },
  {
    id: 100,
    phoneNo: "910098765432",
    status: 3,
    date: getRandomDate()
  }
];