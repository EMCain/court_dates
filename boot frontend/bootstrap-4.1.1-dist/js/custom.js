/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

var JSONmockupPath = '{"question": "How many ducks?","answer": {"1":"All of em!","2":"Some of em!","3":"None of em!"}}'; 
var JSONmockup = JSON.parse(JSONmockupPath);
var question_text = JSONmockup.question;
var unparsed_answers = JSONmockup.answer;

var answer_array = new Array();

for (var key in unparsed_answers) {
<<<<<<< HEAD
    answer_array.push('<a class="btn btn-primary" href="#" data-id="' + key + '">' + unparsed_answers[key] + '</a>');
}

var answer_buttons = answer_array.join('<br>');
=======
    answer_array.push('<a class="btn btn-primary" href="#">' + unparsed_answers[key] + '</a>');
}

var answer_buttons = answer_array.join('')
>>>>>>> 0c28776... moved files and changed gitignore




window.onload = function(){
    document.getElementById('question').innerHTML = question_text;
    document.getElementById('answers').innerHTML = answer_buttons;
};

