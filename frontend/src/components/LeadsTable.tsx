'use client';
import * as React from 'react';
import {
  Box, Button,  Divider, FormControl, FormLabel, Input, Modal, ModalClose,
  ModalDialog, Option, Select, Sheet, Table, Typography, IconButton
} from '@mui/joy';
import {
  FilterAlt as FilterAltIcon,
  Search as SearchIcon,
} from '@mui/icons-material';

import { Lead } from '@/utils';

export default function OrderTable({ rows: incomingRows }: { rows?: Lead[] }) {
  const initialRows = React.useMemo(() => incomingRows || [], [incomingRows]);

  const [rows, setRows] = React.useState<Lead[]>(initialRows);
  const [selectedDate, setSelectedDate] = React.useState<string | null>(null);
  const [selectedStatus, setSelectedStatus] = React.useState<string | null>(null);
  const [searchQuery, setSearchQuery] = React.useState('');
  const [open, setOpen] = React.useState(false);

  const filteredDates = React.useMemo(() => {
    const filtered = initialRows.filter(row =>
      selectedStatus === null ? true : row.stage === Number(selectedStatus)
    );
    return [...new Set(filtered.map(row => row.date))].sort(
      (a, b) => new Date(a).getTime() - new Date(b).getTime()
    );
  }, [initialRows, selectedStatus]);

  const filterData = React.useCallback(() => {
    let filtered = [...initialRows];
    if (selectedStatus !== null) {
      filtered = filtered.filter(row => row.stage === Number(selectedStatus));
    }
    if (selectedDate !== null) {
      filtered = filtered.filter(row => row.date === selectedDate);
    }
    if (searchQuery.trim() !== '') {
      filtered = filtered.filter(row => row.phoneNo.includes(searchQuery));
    }
    setRows(filtered);
  }, [initialRows, selectedStatus, selectedDate, searchQuery]);

  React.useEffect(() => {
    filterData();
  }, [selectedStatus, selectedDate, searchQuery, filterData]);

  const handleClearFilters = () => {
    setSelectedDate(null);
    setSelectedStatus(null);
    setSearchQuery('');
    setRows(initialRows);
  };

  const renderFilters = () => (
    <>
      <FormControl size="sm">
        <FormLabel>Status</FormLabel>
        <Select
          size="sm"
          placeholder="Filter by stage"
          onChange={(_, value) => setSelectedStatus(value)}
          value={selectedStatus || ''}
          slotProps={{ button: { sx: { whiteSpace: 'nowrap' } } }}
        >
          {[1, 2, 3, 4].map(stage => (
            <Option key={stage} value={String(stage)}>{stage}</Option>
          ))}
        </Select>
      </FormControl>
      <FormControl size="sm">
        <FormLabel>Date</FormLabel>
        <Select
          size="sm"
          placeholder="All"
          onChange={(_, value) => setSelectedDate(value)}
          value={selectedDate || ''}
        >
          {filteredDates.map(date => (
            <Option key={date} value={date}>{date}</Option>
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
              <Button onClick={handleClearFilters}>Clear Filters</Button>
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
        className="OrderTableContainer"
        variant="outlined"
        sx={{
          display: { xs: 'none', sm: 'initial' }, width: '100%', borderRadius: 'sm',
          flexShrink: 1, overflow: 'auto', minHeight: 0,
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
              <th style={{ padding: '12px 6px' }}>Phone Number</th>
              <th style={{ padding: '12px 6px' }}>Status</th>
              <th style={{ padding: '12px 6px' }}>Date</th>
            </tr>
          </thead>
          <tbody>
            {[...rows].map(row => (
              <tr key={row.id}>
                <td><Typography level="body-xs" sx={{ px: "30px" }}>{row.id}</Typography></td>
                <td><Typography level="body-xs">{row.phoneNo}</Typography></td>
                <td><Typography level="body-xs">{row.stage}</Typography></td>
                <td><Typography level="body-xs">{row.date}</Typography></td>
              </tr>
            ))}
          </tbody>
        </Table>
      </Sheet>
    </>
  );
}
