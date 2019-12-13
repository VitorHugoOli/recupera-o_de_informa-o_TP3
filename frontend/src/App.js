import React from 'react';

import './App.css';

import logo from './assets/logo.png';


import Routes from './routes'

function App() {
  

  return (
    <>
    
    <div className="container">
      
      <img src={logo} alt="Search City" />
      <div className="content">
      <Routes />
        
        <p>
          Com o <strong>SearchCity</strong> você pode encontrar características de uma determinada cidade, abaixo você pode começar sua pesquisa digitando um termo de busca.
        </p>
      </div>

    </div>
    </>

  );
}

export default App;
