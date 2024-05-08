function toggleVisibility(taskId) {
  var answerDiv = document.getElementById('answer_' + taskId);
  if (answerDiv.style.display === 'none') {
    answerDiv.style.display = 'block';
  } else {
    answerDiv.style.display = 'none';
  }
}

