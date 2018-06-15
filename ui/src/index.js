import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import registerServiceWorker from './registerServiceWorker';
import 'font-awesome/css/font-awesome.css';
import 'primereact/resources/primereact.min.css';

/* THEMES
cruze | cupertino | darkness | flick | home | kasper | lightness | ludvig
omega | pepper-grinder | redmond | rocket | south-street | start | trontastic
voclain */
import 'primereact/resources/themes/kasper/theme.css';


ReactDOM.render(<App />, document.getElementById('root'));
registerServiceWorker();
