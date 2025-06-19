'use client';
import * as React from 'react';
import {
  Box, Button, Divider, FormControl, FormLabel, Input,
  Modal, ModalClose, ModalDialog, Option, Select, Sheet, Table, Typography, IconButton
} from '@mui/joy';
import { FilterAlt as FilterAltIcon, Search as SearchIcon } from '@mui/icons-material';
import axios from '@/utils/axios';

export interface Agent {
  id: number;
  agent: string;
  phoneNo: string;
}

export default function AgentTable() {
  const [rows, setRows] = React.useState<Agent[]>([]);
  const [searchQuery, setSearchQuery] = React.useState('');
  const [selectedAgent, setSelectedAgent] = React.useState<string | null>(null);
  const [open, setOpen] = React.useState(false);

  React.useEffect(() => {
    const fetchLeads = async () => {
      try {
        const response = await axios.get<{ data: Agent[] }>('http://localhost:5000/leads/agents');
        setRows(response.data.data);
      } catch (err) {
        console.error("Error fetching leads:", err);
      }
    };
    fetchLeads();
  }, []);

  const handleClearFilters = () => {
    setSearchQuery('');
    setSelectedAgent(null);
  };

  const filteredRows = rows.filter(row =>
    row.phoneNo.includes(searchQuery)
    && (selectedAgent ? row.agent === selectedAgent : true)
  );

  const renderFilters = () => (
    <>
      <FormControl size="sm">
        <FormLabel>Agent ID</FormLabel>
        <Select
          size="sm"
          placeholder="Filter by Agent"
          onChange={(_, value) => setSelectedAgent(value)}
          value={selectedAgent || ''}
          slotProps={{ button: { sx: { whiteSpace: 'nowrap' } } }}
        >
          {[...new Set(rows.map(row => row.agent))].map(agent => (
            <Option key={agent} value={agent}>{agent}</Option>
          ))}
        </Select>
      </FormControl>
    </>
  );

  return (
    <>
      {/* Mobile Filters */}
      <Sheet className="SearchAndFilters-mobile" sx={{ display: { xs: 'flex', sm: 'none' }, my: 1, gap: 1 }}>
        <Input
          size="sm"
          placeholder="Search"
          startDecorator={<SearchIcon />}
          value={searchQuery}
          onChange={e => setSearchQuery(e.target.value)}
          sx={{ flexGrow: 1 }}
        />
        <IconButton size="sm" variant="outlined" color="neutral" onClick={() => setOpen(true)}>
          <FilterAltIcon />
        </IconButton>
        <Modal open={open} onClose={() => setOpen(false)}>
          <ModalDialog layout="fullscreen" aria-labelledby="filter-modal">
            <ModalClose />
            <Typography level="h2" id="filter-modal">Filters</Typography>
            <Divider sx={{ my: 2 }} />
            <Sheet sx={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
              {renderFilters()}
              <Button color="primary" onClick={() => setOpen(false)}>Apply</Button>
              <Button variant="outlined"  onClick={handleClearFilters}>
                Clear Filters
              </Button>
            </Sheet>
          </ModalDialog>
        </Modal>
      </Sheet>

      {/* Desktop Filters */}
      <Box
        className="SearchAndFilters-tabletUp"
        sx={{
          borderRadius: 'sm', py: 2, display: { xs: 'none', sm: 'flex' }, flexWrap: 'wrap', gap: 1.5,
          '& > *': { minWidth: { xs: '120px', md: '160px' } },
        }}
      >
        <FormControl sx={{ flex: 1 }} size="sm">
          <FormLabel>Search for WhatsApp Number</FormLabel>
          <Input
            size="sm"
            placeholder="Search"
            startDecorator={<SearchIcon />}
            value={searchQuery}
            onChange={e => setSearchQuery(e.target.value)}
          />
        </FormControl>
        {renderFilters()}
        <Box sx={{ display: 'flex', alignItems: 'flex-end' }}>
          <Button  size="sm" onClick={handleClearFilters}>
            Clear Filters
          </Button>
        </Box>
      </Box>

      {/* Table */}
      <Sheet
        className="AgentTableContainer"
        variant="outlined"
        sx={{
          display: { xs: 'none', sm: 'initial' },
          width: '100%',
          borderRadius: 'sm',
          overflow: 'auto',
        }}
      >
        <Table
          stickyHeader
          hoverRow
          sx={{
            '--TableCell-headBackground': 'var(--joy-palette-background-level1)',
            '--Table-headerUnderlineThickness': '1px',
            '--TableRow-hoverBackground': 'var(--joy-palette-background-level1)',
            '--TableCell-paddingY': '4px',
            '--TableCell-paddingX': '8px',
          }}
        >
          <thead>
            <tr>
              <th style={{ padding: '12px 30px' }}>ID</th>
              <th>Agent ID</th>
              <th>Phone Number</th>
            </tr>
          </thead>
          <tbody>
            {filteredRows.length === 0 ? (
              <tr>
                <td colSpan={3}>
                  <Typography level="body-sm" textAlign="center" sx={{ py: 2 }}>
                    No data available
                  </Typography>
                </td>
              </tr>
            ) : (
              filteredRows.map(row => (
                <tr key={row.id}>
                  <td><Typography level="body-xs" sx={{ px: "30px" }}>{row.id}</Typography></td>
                  <td><Typography level="body-xs">{row.agent}</Typography></td>
                  <td><Typography level="body-xs">{row.phoneNo}</Typography></td>
                </tr>
              ))
            )}
          </tbody>
        </Table>
      </Sheet>
    </>
  );
}
