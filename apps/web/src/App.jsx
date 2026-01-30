import { useState } from 'react'
import './App.css'

function App() {
  const [url, setUrl] = useState('')
  const [status, setStatus] = useState('Idle')

  const handleClip = async () => {
    setStatus('Requesting...')
    try {
        const response = await fetch(`http://localhost:8000/process-video?url=${encodeURIComponent(url)}`, {
            method: 'POST'
        })
        const data = await response.json()
        setStatus(`Server says: ${data.message}`)
    } catch (e) {
        setStatus('Error connecting to backend')
    }
  }

  return (
    <div style={{ padding: '2rem', fontFamily: 'sans-serif' }}>
      <h1>✂️ Omni-Clipper Dashboard</h1>
      <div style={{ display: 'flex', gap: '10px', marginBottom: '20px' }}>
        <input 
            type="text" 
            placeholder="Paste YouTube URL..." 
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            style={{ padding: '10px', width: '300px' }}
        />
        <button onClick={handleClip} style={{ padding: '10px 20px', cursor: 'pointer' }}>
            Generate Clips
        </button>
      </div>
      <div style={{ padding: '20px', background: '#f0f0f0', borderRadius: '8px' }}>
        <strong>Status:</strong> {status}
      </div>
    </div>
  )
}

export default App
