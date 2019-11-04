import React, {useEffect, useState} from 'react';
import {Link} from 'react-router-dom'
import api from '../../services/api';

import './styles.css';

export default function Results(){
    
    const [results, setResults] = useState([])

    useEffect(() => {
        async function loadResults(){
            const termo = localStorage.getItem('searchterm')
            const response = await api.get('/search/'+termo)
            var lista = [];
            //const response = await api.get('./texto/1');
            console.log(response.data.relevance);
            const resultado = response.data.relevance;
            for (const key in resultado) {
                if (resultado.hasOwnProperty(key)) {
                    const relevance = resultado[key];
                    const element = await api.get('/texto/'+key)
                    lista.push({key, relevance, element})
                    
                }
            }
            console.log(lista)
            setResults(lista);
        }
        
        loadResults();
    }, [])
    
    return (
        <>
            <ul className="result-list">
                
                
            {results.map(result => (
                <Link to='/details' onClick={() => (
                    localStorage.setItem('textoid', result.key)
                )}>
                    <li key={result.key}>
                        {result.key}
                        <strong>{result.element.data.Titulo}</strong>
                        <span>Relevância: {result.relevance}</span>

                    </li>
                </Link>
            ))}
                
               
                
            </ul>
        </>
    )
}

/*{results.map(result => (
    <Link to="/details">
        <li key={result._id}>
            <strong>{result.Titulo}</strong>
            <span>Relevância: {result.Texto}</span>

        </li>
    </Link>
))}*/

/*{results.map(result => (
    <li key={result._id}>
        <strong>{result.title}</strong>
        <span>Relevância: {result.relevance}</span>

    </li>
))}*/