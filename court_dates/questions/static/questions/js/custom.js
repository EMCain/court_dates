/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

const JSONmockupPath = '{"question": "How many ducks?","answer": {"1":"All of em!","2":"Some of em!","3":"None of em!"}}'; 
const JSONmockup = JSON.parse(JSONmockupPath);

let currentQuestionID = 1; // holds "state" of the current question; will change TODO remove hardcoded

function loadQuestionData(data) { 
    const question_text = data.question;
    const unparsed_answers = data.answers;


    document.getElementById('question').innerHTML = question_text;

    $('#answers').html('');
    for (const key in unparsed_answers) {
        const new_button = $('<a class="btn btn-primary" href="#" data-id="' + key + '">' + unparsed_answers[key] + '</a>');
        new_button.click(sendAnswer);
        $('#answers').append(new_button);
    }
}

function setQuestion(questionID) {
    currentQuestionID = questionID;
    // send an api requiest 
    // load question data with the results 
    const url = '/api/ask/' + currentQuestionID;
    console.log(url);
    $.getJSON(url, loadQuestionData);
}

function sendAnswer(event) {
    event.preventDefault();
    const target = event.target;
    const answerId = target.dataset.id;
    const url = '/api/ask/' + currentQuestionID + '/answer/' + answerId;
    $.getJSON(url, function(data) {
        setQuestion(data.id);
    });
}
$(function(){
    setQuestion(currentQuestionID);
});

// TODO 
// set the question ID 
// call LoadQuestionData based on the question ID
// for each button: 
// give it a listener
// when you click the button 
// send its data-id as an answer to the current question 

