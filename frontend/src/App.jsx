import { useState,useRef } from 'react';
import Typewriter from 'typewriter-effect';
import Input from './Input';

export default function App() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [result, setResult] = useState(null);
  const fileInputRef = useRef(null);

  const handleUpload = async () => {
    if (!selectedFile) {
      alert('Please select a file first!');
      return;
    }
    const formData = new FormData();
    formData.append('file', selectedFile);

    try {
      const response = await fetch('/api/predict', {
        method: 'POST',
        body: formData,
      });
      const data = await response.json();
      setSelectedFile(null)
      setResult(data)
      

    } catch (error) {
      console.error('Error uploading file:', error);
    }
  }

  const handleClear = () => {
    if (fileInputRef.current) {
      setSelectedFile(null);
      setResult(null)
      fileInputRef.current.value = "";
    }
  }  


  return (
    <div className="flex justify-between items-center h-screen bg-[rgb(15,15,16)]">
      <div className="text-[rgb(209,197,173)] p-8 ml-40">
        <h1 className="text-6xl font-bold">Image Classifier</h1>
        <p className="text-2xl mt-4 mb-24">Upload an image to classify it.</p>
        <Input fileInputRef={fileInputRef} setSelectedFile={setSelectedFile} selectedFile={selectedFile} />
      </div>
      <div className='flex flex-col mr-40'>
        <div className='w-full h-48 bg-[rgb(146,138,121)] rounded-xl font-bold text-lg border-dashed flex justify-center items-center'>
          {result ? <Typewriter
            options={{
              strings: ['The image is that of a ' + result?.predicted_class],
              autoStart: true,
              loop: true,
              pauseFor: 1000000,
            }}
          /> : <Typewriter
            options={{
              strings: ["Awaiting upload..."],
              autoStart: true,
              loop: true,
            }}
          />}
        </div>
        <div className="flex  justify-between mr-40 w-full">
          <button className="bg-indigo-500 hover:bg-indigo-600 text-white font-bold mt-4 px-4 py-2 rounded" onClick={handleUpload}>Upload Image</button>
          <button className="bg-indigo-500 hover:bg-indigo-600 text-white font-bold mt-4 px-6 py-2 rounded" onClick={handleClear}>Clear input</button>
        </div>
      </div>
    </div>
  );
}

