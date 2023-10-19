const equivalents = [
  { bare: "А", apostraphe: "А'", accent: "А́" },
  { bare: "Е", apostraphe: "Е'", accent: "Е́" },
  { bare: "И", apostraphe: "И'", accent: "И́" },
  { bare: "О", apostraphe: "О'", accent: "О́" },
  { bare: "У", apostraphe: "У'", accent: "У́" },
  { bare: "Ы", apostraphe: "Ы'", accent: "Ы́" },
  { bare: "Э", apostraphe: "Э'", accent: "Э́" },
  { bare: "Ю", apostraphe: "Ю'", accent: "Ю́" },
  { bare: "Я", apostraphe: "Я'", accent: "Я́" },
  { bare: "а", apostraphe: "а'", accent: "а́" },
  { bare: "е", apostraphe: "е'", accent: "е́" },
  { bare: "и", apostraphe: "и'", accent: "и́" },
  { bare: "о", apostraphe: "о'", accent: "о́" },
  { bare: "у", apostraphe: "у'", accent: "у́" },
  { bare: "ы", apostraphe: "ы'", accent: "ы́" },
  { bare: "э", apostraphe: "э'", accent: "э́" },
  { bare: "ю", apostraphe: "ю'", accent: "ю́" },
  { bare: "я", apostraphe: "я'", accent: "я́" }
];

const outputFunctions = {
  removeAccentsAndApostraphes: function (inputStr) {
    let outputStr = inputStr;
    equivalents.forEach((eq) => {
      outputStr = outputStr.replaceAll(eq.apostraphe, eq.bare);
      outputStr = outputStr.replaceAll(eq.accent, eq.bare);
    });
    return outputStr;
  },
  replaceApostraphesWithAccents: function (inputStr) {
    let outputStr = inputStr;
    equivalents.forEach((eq) => {
      outputStr = outputStr.replaceAll(eq.apostraphe, eq.accent);
    });
    return outputStr;
  },
  replaceAccentsWithApostraphes: function (inputStr) {
    let outputStr = inputStr;
    equivalents.forEach((eq) => {
      outputStr = outputStr.replaceAll(eq.accent, eq.apostraphe);
    });
    return outputStr;
  },
  // addStressMarks: function (inputStr) {
  //   const bare = outputFunctions["removeAccentsAndApostraphes"](inputStr);
  //   const unique = getUniqueWhitespaceSeparatedWords(bare);
  //   const stressed = serverEndpointAddStressMarks(unique);
  //   const apostrapheStr = replaceLowerAndTitleCase(bare, unique, stressed);
  //   return outputFunctions["replaceApostraphesWithAccents"](apostrapheStr);
  // },
  // replaceWordsWithDictionaryForms: function (inputStr) {
  //   const bare = outputFunctions["removeAccentsAndApostraphes"](inputStr);
  //   const unique = getUniqueWhitespaceSeparatedWords(bare);
  //   const dictionary = serverEndpointGetDictionaryForm(unique);
  //   const apostrapheStr = replaceLowerAndTitleCase(bare, unique, dictionary);
  //   return outputFunctions["replaceApostraphesWithAccents"](apostrapheStr);
  // }
};

// const getUniqueWhitespaceSeparatedWords = (inputStr) => {
//   // https://stackoverflow.com/a/31779560/10568900
//   const lowerCase = inputStr.toLowerCase();
//   const noPunctuation = lowerCase.replace(
//     /[~`!@#$%^&*(){}\[\];:"'<,.>?\/\\|_+=-]/g,
//     ""
//   );
//   return [...new Set(noPunctuation.split(/\s+/))]; // whitespace separated
// };

// const replaceLowerAndTitleCase = (inputStr, searchForList, replaceWithList) => {
//   let outputStr = inputStr;
//   for (let i = 0; i < searchForList.length; i++) {
//     // skip if no replacement
//     if (replaceWithList[i] == null) {
//       continue;
//     }

//     // replace lower case
//     const searchForLowerCase = searchForList[i].toLowerCase();
//     const replaceWithLowerCase = replaceWithList[i].toLowerCase();
//     const reSearchLowerCase = new RegExp(searchForLowerCase, "g");
//     outputStr = outputStr.replace(reSearchLowerCase, replaceWithLowerCase);

//     // replace title case
//     const searchForTitleCase = searchForLowerCase.replace(
//       searchForLowerCase[0],
//       searchForLowerCase[0].toUpperCase()
//     );
//     const replaceWithTitleCase = replaceWithLowerCase.replace(
//       replaceWithLowerCase[0],
//       replaceWithLowerCase[0].toUpperCase()
//     );
//     const reSearchForTitleCase = new RegExp(searchForTitleCase, "g");
//     outputStr = outputStr.replace(reSearchForTitleCase, replaceWithTitleCase);
//   }
//   return outputStr;
// };

// const serverEndpointAddStressMarks = (wordsList) => {
//   //  returns array of accented equivalent(s) for each item in wordsList
//   //  wordsList.length == returnArray.length
//   //  if no accented equivalent for item, insert null into returnArray
//   //  if multiple equivalents, insert each separated by |
//   //    eg писать --> писа'ть|пи'сать
//   //  accented equivalent may just replace е for ё

//   //  this is a fake imitation of what the server would do for this wordsList
//   //  wordsList = ["говорю", "писать", "вернемся", "english"];
//   const returnArray = ["говорю'", "писа'ть|пи'сать", "вернёмся", null];
//   return returnArray;
// };

// const serverEndpointGetDictionaryForm = (wordsList) => {
//   //  returns array of dictionary forms for each item in wordsList
//   //  wordsList.length == returnArray.length
//   //  if no dictionary form for item, insert null into returnArray
//   //  if item already in dictionary form (without accent), insert dictionary form into returnArray
//   //  if multiple possible dictionary forms, insert each separated by |
//   //    eg замок --> замо'к|за'мок

//   //  this is a fake imitation of what the server would do for this wordsList
//   //  wordsList = ["говорю", "говорить", "замок", "english"];
//   const returnArray = ["говоти'ть", "говори'ть", "замо'к|за'мок", null];
//   return returnArray;
// };

const onSubmit = () => {
  const textInput = document.getElementById("textInput");
  const functionToUse = document.querySelector(`[name="radioOuput"]:checked`)
    .id;
  const inputStr = textInput.value;
  const val = outputFunctions[functionToUse](inputStr);
  textInput.value = outputFunctions[functionToUse](inputStr);
};

document.getElementById("btnSubmit").addEventListener("click", onSubmit);