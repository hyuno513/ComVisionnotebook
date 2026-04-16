function changeText() {
    // 1. HTML에서 id가 'title'인 요소를 찾는 과정
    const titleElement = document.getElementById('title');

    // 2. 그 요소 내용을 변경
    titleElement.innerText = "자바스크립트로 바꿨습니다.★"

    // 3. 스타일 바꾸기
    titleElement.style.color = 'blue';


}

const button = document.getElementById('btn');
const title = document.getElementById('main-title')
button.addEventListener('click', function () {
    title.style.color = 'orange';
    title.innerText = 'JS파일'
    alert('클릭되었습니다.')
    console.log('버튼이 클릭되었습니다.')
})