/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

const JSONmockupPath = '{"question": "How many ducks?","answer": {"1":"All of em!","2":"Some of em!","3":"None of em!"}}'; 
const JSONmockup = JSON.parse(JSONmockupPath);


function loadQuestionData(data) {
    const question_text = data.question;
    const unparsed_answers = data.answer;

    let answer_array = new Array();

    for (const key in unparsed_answers) {
        answer_array.push('<a class="btn btn-primary" href="#" data-id="' + key + '">' + unparsed_answers[key] + '</a>');
    }
    const answer_buttons = answer_array.join('<br>');

    document.getElementById('question').innerHTML = question_text;
    document.getElementById('answers').innerHTML = answer_buttons;
}


window.onload = function(){
    loadQuestionData(JSONmockup)
};

