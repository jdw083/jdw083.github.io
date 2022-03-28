const axios = require("axios");
const cheerio = require("cheerio");

//fetch redirect URLs for all schools
const fetchResults = async () => {
    try {
        const response = await axios.get('https://ia.varsitybound.com/schools/');
        const html = response.data;
        const $ = cheerio.load(html);
        const results = [];
        $('a:contains("Directory")').each((_idx, el) => {
            const result = $(el).attr('href');
            results.push(result);
        });

        //console.log(results.length);      //here for testing
        
        //for each school, navigate to the respective directory page
        for (let i = 0; i < results.length; i++) {
            var str = results[i];
            //console.log(str);     //here for testing
                var responseTwo = await axios.get('https://ia.varsitybound.com' + str);
                var htmlTwo = responseTwo.data;
                var $Two = cheerio.load(htmlTwo);
                var resultsDir = [];
                
            //pull the text that contains 'golf'
                $Two('div.card.p2.mx-1.my-2:contains("Golf")').each((_idx, el) => {
                    var resultTwo = $Two(el).text();
                    //console.log(resultTwo)    //here for testing
                    resultsDir.push(resultTwo);
                });
            //cool little progress meter to make sure it is working...
            console.log('Record ' + i + ' completed. Working on record ' + (i + 1) + '...');
        };
        return resultsDir;
    } catch (error) {
        throw error;
    };
};
fetchResults().then((resultsDir) => console.log(resultsDir));

