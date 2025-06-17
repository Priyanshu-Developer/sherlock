"use client";
import Dashboard from "@/components/Dashboard";
import AgentTable from "@/components/AgentTable";
import Snackbar from '@mui/joy/Snackbar';


import {  useState } from "react";

export default function LeadsPage() {
  
  const [snackbarOpen, setSnackbarOpen] = useState(false);
  return (
    <>
      <Dashboard>
        <AgentTable  />
      </Dashboard>
      <Snackbar
        open={snackbarOpen}
        autoHideDuration={6000}
        onClose={() => setSnackbarOpen(false)}
        variant="soft"
        color="danger"
        anchorOrigin={{ vertical: 'top', horizontal: 'center' }}
      >
        Failed to fetch Agents. Please try again later.
      </Snackbar>
    </>
  );
}