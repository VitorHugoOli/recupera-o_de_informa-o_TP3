import React, {useState, useMemo} from 'react';


import './styles.css'
import fileimg from '../../assets/file.png'


export default function NewUpload(){
    const [title, setTitle] = useState('');
    const [file, setFile] = useState(null);

    const preview = useMemo(
        () => {
            return file ? URL.createObjectURL(file) : null;
        },
        [file]
    )

    function handleSubmit(){

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
            <label id="thumbnail">
                <input 
                    type="file" 
                    placeholder="Selecione um arquivo"
                    onChange={event => setFile(event.target.files[0])}
                />
                <img src={fileimg} alt="Selecione o arquivo"/>
            </label>
            
            <button type="submit"  onClick={handleSubmit}>
                Upload
            </button>
        </form>
    );
}