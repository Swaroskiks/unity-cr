import axios from 'axios';

const API_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:5001';

export interface FileItem {
    path: string;
    name: string;
    type: 'file' | 'directory';
}

export default {
    async listFiles(): Promise<string[]> {
        const response = await axios.get(`${API_URL}/files`);
        return response.data;
    },

    async getFile(path: string): Promise<string> {
        const response = await axios.get(`${API_URL}/files/${path}`);
        return response.data.content;
    },

    async saveFile(filename: string, content: string): Promise<void> {
        await axios.post(`${API_URL}/files`, { filename, content });
    },

    async uploadImage(file: File): Promise<string> {
        const formData = new FormData();
        formData.append('file', file);
        const response = await axios.post(`${API_URL}/images`, formData, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        });
        return response.data.url;
    },

    async uploadAudio(file: File): Promise<string> {
        const formData = new FormData();
        formData.append('file', file);
        const response = await axios.post(`${API_URL}/audio`, formData, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        });
        return response.data.url;
    }
};
