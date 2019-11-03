import React from 'react';
import './App.css';

import logo from './assets/logo.png';
import search from './assets/search.png';

function App() {
  return (
    <>
    <div className="upload">
      <button type="button">
        Fazer Upload
      </button>
    </div>
    <div className="container">
      
      <img src={logo} alt="Search City"/>
      <div className="content">
        
        
        <div className="search">
          <input type="text" id="searchtext" placeholder="Faça sua busca aqui"/>
          <button type="submit" className="search">
             <img src={search} alt="Search City"/>
          </button>
        </div>

        <p>
          Com o <strong>SearchCity</strong> você pode encontrar características de uma determinada cidade, abaixo você pode começar sua pesquisa digitando um termo de busca.
        </p>
      </div>

    </div>
    </>

  );
}

export default App;
