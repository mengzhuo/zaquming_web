<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width">
        % if title:
        <title>{{title}} - 咋取名</title>
        % else:
        <title>咋取名</title>
        % end
        <style>
        html {text-align:center}
        @keyframes enter { from {opacity:0.1;} to {opacity:1;} }
        @-webkit-keyframes enter { from {opacity:0.1;} to {opacity:1;} }
        @keyframes focus { from {box-shadow:green 0 0 0px;} to {box-shadow:green 0 0 4px;} }
        @-webkit-keyframes focus { from {box-shadow:green 0 0 0px;} to {box-shadow:green 0 0 4px;} }

        @keyframes text-focus {from {color:black;} to {color:green;font-size:1.1em;padding:1px;}}
        body {font-family:arial,sans-serif;background:#fffaf0;animation:enter 0.5s ease-out;vertical-align:middle;line-height:1em;text-align:left;position:relative;left:40%;float:left;}
        a {text-decoration:none;}
        #index {text-align:center;padding-top:10px;font-family:monospace;}
        #index .keyword {opacity:0.4;}
        input, button {padding:0.2em;font-size:1em;border-radius:5px;border:1px solid #ccc;background:white;}
        input:focus, button:focus, button:hover, input:hover {outline:none;border:1px solid #999;box-shadow:green 0 0 4px;animation: focus 0.5s linear;}
        button {padding:0.2em 1em;cursor:pointer;}#searchform {margin:0.5em 1em;}
        dd {padding:1px 0;}dt{font-style: italic;}
        dd:hover {animation:text-focus 0.5s ease-in; color:green;font-size:1.1em;padding:1px;}
        .add_word{opacity:0}
        .add_word:hover,.add_word:focus {opacity:1;animation:enter 0.3s ease-out;}
        .add_word input {margin:3px 0;}
        </style>
    </head>
    <body>

    <a href="https://github.com/mengzhuo/zaquming_web"><img style="position: fixed; top: 0; right: 0; border: 0;" src="https://camo.githubusercontent.com/e7bbb0521b397edbd5fe43e7f760759336b5e05f/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f6769746875622f726962626f6e732f666f726b6d655f72696768745f677265656e5f3030373230302e706e67" alt="Fork me on GitHub" data-canonical-src="https://s3.amazonaws.com/github/ribbons/forkme_right_green_007200.png"></a>
