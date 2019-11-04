import React from 'react'

import {BrowserRouter, Switch, Route} from 'react-router-dom';


import NewUpload from './pages/NewUpload';
import Search from './pages/Search';
import Details from './pages/Details';
import Results from './pages/Results';


export default function Routes(){
    return (
        <BrowserRouter>
            <Switch>
                <Route path="/" exact component={Search}/>
                <Route path="/results" component={Results}/>
                <Route path="/details" component={Details}/>
                <Route path="/newupload" component={NewUpload}/>
            </Switch>
        </BrowserRouter>
    );
}