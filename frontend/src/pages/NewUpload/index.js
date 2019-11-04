import React, {useState, useMemo} from 'react';


import './styles.css'
import fileimg from '../../assets/file.png'
import api from '../../services/api';


export default function NewUpload({history}){
    const [title, setTitle] = useState('');
    const [file, setFile] = useState(null);

    const preview = useMemo(
        () => {
            return file ? URL.createObjectURL(file) : null;
        },
        [file]
    )

    async function handleSubmit(event){
        event.preventDefault();
        const data = new FormData();
        
        
       
        data.append('title,', title);
        data.append('file,', file);
        
        console.log(title)
        console.log(file)
        await api.post('/uploadFile', data);

        history.push('/')
    }

    return (
        <form onSubmit={handleSubmit} className="upload">
            <label htmlFor="company"> Título *</label>
            
            <input 
                type="text" 
                id="title" 
                placeholder="Qual o título do texto?"
                value={title}
                onChange={event => setTitle(event.target.value)}
            />
            <label 
                id="thumbnail"
                className={file ? 'has-file' : ''}
            >
                <input 
                    type="file" 
                    placeholder="Selecione um arquivo"
                    onChange={event => setFile(event.target.files[0])}
                />
                <strong>{file ? file.name : ''}</strong>
                <img src={fileimg} alt="Selecione o arquivo"/>
            </label>
            
            <button type="submit"  onClick={handleSubmit}>
                Upload
            </button>
        </form>
    );
}