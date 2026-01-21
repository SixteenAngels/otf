import React, { useState, useEffect } from 'react';
import { QRScanner } from '../components/QRScanner';
import { scanAPI, ticketAPI, concertAPI } from '../api/client';
import { useAuthStore } from '../store';
import { toast } from 'react-toastify';

const statusColors = {
  created: 'bg-gray-100 text-gray-800',
  sold: 'bg-blue-100 text-blue-800',
  verified: 'bg-green-100 text-green-800',
  attended: 'bg-purple-100 text-purple-800',
  duplicate: 'bg-yellow-100 text-yellow-800',
  refunded: 'bg-red-100 text-red-800',
  transferred: 'bg-indigo-100 text-indigo-800',
};

export const ScannerPage = () => {
  const [scanType, setScanType] = useState('attendance');
  const [location, setLocation] = useState('');
  const [scannedTicket, setScannedTicket] = useState(null);
  const [scannedConcert, setScannedConcert] = useState(null);
  const [loading, setLoading] = useState(false);
  const user = useAuthStore((state) => state.user);

  const handleScan = async (qrData) => {
    try {
      const ticket = await ticketAPI.getByNumber(qrData.ticket_number);
      
      const isVerifier = user?.username?.startsWith('verify');
      
      if (isVerifier && ticket.status === 'attended') {
        toast.error('❌ Ticket already attended - cannot rescan!');
        setScannedTicket(null);
        return;
      }
      
      setScannedTicket(ticket);
      
      try {
        const concert = await concertAPI.get(ticket.concert_id);
        setScannedConcert(concert);
      } catch (err) {
        setScannedConcert(null);
      }

      setLoading(true);
      await scanAPI.create({
        ticket_id: ticket.id,
        scan_type: scanType,
        location: location || undefined,
      });

      if (isVerifier) {
        toast.success(`✓ Ticket marked as attended!`);
      } else {
        toast.success(`Ticket scan recorded - Status: ${scanType}`);
      }
      
      // Refresh ticket state
      const updatedTicket = await ticketAPI.getByNumber(qrData.ticket_number);
      setScannedTicket(updatedTicket);

      setTimeout(() => {
        setScannedTicket(null);
        setScannedConcert(null);
      }, 4000);
    } catch (error) {
      toast.error(error.response?.data?.detail || 'Scan failed');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 py-12 px-4">
      <div className="max-w-2xl mx-auto">
        <h1 className="text-3xl font-bold text-gray-900 mb-2">Ticket Scanner</h1>
        <p className="text-gray-600 mb-8">
          {user?.username?.startsWith('verify') 
            ? '🔒 Attendance Mode - Each ticket can only be scanned ONCE' 
            : '📝 Sales/Admin Mode - Multiple scans allowed'}
        </p>

        <div className="bg-white rounded-lg shadow p-6 mb-6">
          <div className="mb-6">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Scan Type
            </label>
            <select
              value={scanType}
              onChange={(e) => setScanType(e.target.value)}
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-blue-500 focus:border-blue-500"
            >
              <option value="attendance">Attendance</option>
              <option value="sale">Sale</option>
            </select>
          </div>

          <div className="mb-6">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Location (optional)
            </label>
            <input
              type="text"
              value={location}
              onChange={(e) => setLocation(e.target.value)}
              placeholder="Gate 1, Entrance A, etc."
              className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-blue-500 focus:border-blue-500"
            />
          </div>

          <QRScanner onScan={handleScan} />

          {scannedTicket && (
            <div className={`mt-6 p-4 border rounded ${scannedTicket.status === 'attended' ? 'bg-purple-50 border-purple-200' : 'bg-green-50 border-green-200'}`}>
              <h3 className={`text-lg font-semibold mb-3 ${scannedTicket.status === 'attended' ? 'text-purple-900' : 'text-green-900'}`}>
                ✓ Ticket Scanned Successfully
              </h3>
              
              {scannedConcert && (
                <div className="mb-4 pb-4 border-b border-gray-200">
                  <p className="font-bold text-base">
                    {scannedConcert.name}
                  </p>
                  <p className="text-sm">
                    <strong>Venue:</strong> {scannedConcert.venue}
                  </p>
                  <p className="text-sm">
                    <strong>Date:</strong> {new Date(scannedConcert.date).toLocaleDateString()}
                  </p>
                </div>
              )}
              
              <div className="space-y-1 text-sm">
                <p>
                  <strong>Ticket:</strong> {scannedTicket.ticket_number}
                </p>
                <p>
                  <strong>Buyer:</strong> {scannedTicket.buyer_name || 'N/A'}
                </p>
                <p>
                  <strong>Email:</strong> {scannedTicket.buyer_email || 'N/A'}
                </p>
                <p className={`font-semibold`}>
                  <strong>Status:</strong> 
                  <span className={`ml-2 px-2 py-1 rounded text-xs font-mono ${statusColors[scannedTicket.status] || 'bg-gray-100 text-gray-800'}`}>
                    {scannedTicket.status}
                  </span>
                </p>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default ScannerPage;
