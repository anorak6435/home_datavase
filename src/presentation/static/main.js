console.log("Loaded the main file from static folder!");
let mirrors = []; // the code mirror editors from text areas
function code_textareas() {
    let code_areas = Array.from(document.getElementsByClassName("code"));
    console.log(code_areas);
    code_areas.forEach((area) => {
        mirrors.push(CodeMirror.fromTextArea(area, {lineNumbers: true, theme: "dracula"}))
    });
} 


code_textareas();