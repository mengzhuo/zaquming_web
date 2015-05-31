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
        @keyframes enter { from {opacity:0.1;} to {opacity:1;} }
        @-webkit-keyframes enter { from {opacity:0.1;} to {opacity:1;} }
        @keyframes focus { from {box-shadow:green 0 0 0px;} to {box-shadow:green 0 0 4px;} }
        @-webkit-keyframes focus { from {box-shadow:green 0 0 0px;} to {box-shadow:green 0 0 4px;} }
        body {font-family:arial,sans-serif;background:#fffaf0;animation:enter 0.5s ease-out;vertical-align:middle;line-height:1em;}
        a {text-decoration:none;}
        #index {text-align:center;padding-top:100px;font-family:monospace;}
        #index .keyword {opacity:0.4;}
        input, button {padding:0.2em;font-size:1em;border-radius:5px;border:1px solid #ccc;background:white;}
        input:focus, button:focus, button:hover, input:hover {outline:none;border:1px solid #999;box-shadow:green 0 0 4px;animation: focus 0.5s linear;}
        button {padding:0.2em 1em;cursor:pointer;}
#searchform {margin:0.5em 1em;}
        </style>
    </head>
    <body>
