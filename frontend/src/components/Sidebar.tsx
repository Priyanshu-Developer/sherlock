import * as React from 'react';
import GlobalStyles from '@mui/joy/GlobalStyles';
import Avatar from '@mui/joy/Avatar';
import Box from '@mui/joy/Box';
import Chip from '@mui/joy/Chip';
import Divider from '@mui/joy/Divider';
import IconButton from '@mui/joy/IconButton';
import List from '@mui/joy/List';
import ListItem from '@mui/joy/ListItem';
import ListItemButton, { listItemButtonClasses } from '@mui/joy/ListItemButton';
import ListItemContent from '@mui/joy/ListItemContent';
import Typography from '@mui/joy/Typography';
import Sheet from '@mui/joy/Sheet';

import LogoutRoundedIcon from '@mui/icons-material/LogoutRounded';
import BrightnessAutoRoundedIcon from '@mui/icons-material/BrightnessAutoRounded';
import KeyboardArrowDownIcon from '@mui/icons-material/KeyboardArrowDown';

import ColorSchemeToggle from './ColorSchemeToggle';
import { closeSidebar } from '../utils';
import Link from 'next/link';
import { usePathname } from 'next/navigation';

interface TogglerProps {
  defaultExpanded?: boolean;
  renderToggle: (params: {
    open: boolean;
    setOpen: React.Dispatch<React.SetStateAction<boolean>>;
  }) => React.ReactNode;
  children: React.ReactNode;
}

function Toggler({defaultExpanded = false,renderToggle,children,}: TogglerProps) {
  const [open, setOpen] = React.useState(defaultExpanded);
  return (
    <React.Fragment>
      {renderToggle({ open, setOpen })}
      <Box
        sx={[
          {
            display: 'grid',
            transition: '0.2s ease',
            '& > *': {
              overflow: 'hidden',
            },
          },
          open ? { gridTemplateRows: '1fr' } : { gridTemplateRows: '0fr' },
        ]}
      >
        {children}
      </Box>
    </React.Fragment>
  );
}
interface MenuProps {
  title: string;
  icon: React.ReactNode;
  segment: string;
  children?: MenuProps[];
  chipCount?: number;
}

interface CustomMenuProps {
  menu: MenuProps[];
  currentPath: string; // e.g., useRouter().pathname
}

export const CustomMenu: React.FC<CustomMenuProps> = ({menu,currentPath}) => {
  const renderMenuItems = (items: MenuProps[]) => {
    return items.map((item, index) => {
      const isSelected = currentPath === item.segment;

      if (item.children && item.children.length > 0) {
        return (
          <ListItem nested key={index}>
            <Toggler
              renderToggle={({ open, setOpen }) => (
                <ListItemButton onClick={() => setOpen(!open)}>
                  {item.icon}
                  <ListItemContent>
                    <Typography level="title-sm">{item.title}</Typography>
                  </ListItemContent>
                  <KeyboardArrowDownIcon
                    sx={{
                      transform: open ? "rotate(180deg)" : "none",
                      transition: "0.3s"
                    }}
                  />
                </ListItemButton>
              )}
            >
              <List sx={{ gap: 0.5 }}>{renderMenuItems(item.children)}</List>
            </Toggler>
          </ListItem>
        );
      }

      return (
        <ListItem key={index}>
          <Link href={item.segment} passHref legacyBehavior>
            <ListItemButton component="a" selected={isSelected}>
              {item.icon}
              <ListItemContent>
                <Typography level="title-sm">{item.title}</Typography>
              </ListItemContent>
              {item.chipCount && (
                <Chip size="sm" color="primary" variant="solid">
                  {item.chipCount}
                </Chip>
              )}
            </ListItemButton>
          </Link>
        </ListItem>
      );
    });
  };
  return <List  size="sm"
          sx={{
            gap: 1,
            '--List-nestedInsetStart': '30px',
            '--ListItem-radius': (theme) => theme.vars.radius.sm,
          }}>{renderMenuItems(menu)}</List>;
};

interface SidebarProps {
  menuItems: MenuProps[];
  pathname: string;
}

export default function Sidebar({menuItems}: SidebarProps) {
  const currentPath = usePathname();
  return (
    <Sheet
      className="Sidebar"
      sx={{
        position: { xs: 'fixed', md: 'sticky' },
        transform: {
          xs: 'translateX(calc(100% * (var(--SideNavigation-slideIn, 0) - 1)))',
          md: 'none',
        },
        transition: 'transform 0.4s, width 0.4s',
        zIndex: 10000,
        height: '100dvh',
        width: 'var(--Sidebar-width)',
        top: 0,
        p: 2,
        flexShrink: 0,
        display: 'flex',
        flexDirection: 'column',
        gap: 2,
        borderRight: '1px solid',
        borderColor: 'divider',
      }}
    >
      <GlobalStyles
        styles={(theme) => ({
          ':root': {
            '--Sidebar-width': '220px',
            [theme.breakpoints.up('lg')]: {
              '--Sidebar-width': '240px',
            },
          },
        })}
      />
      <Box
        className="Sidebar-overlay"
        sx={{
          position: 'fixed',
          zIndex: 9998,
          top: 0,
          left: 0,
          width: '100vw',
          height: '100vh',
          opacity: 'var(--SideNavigation-slideIn)',
          backgroundColor: 'var(--joy-palette-background-backdrop)',
          transition: 'opacity 0.4s',
          transform: {
            xs: 'translateX(calc(100% * (var(--SideNavigation-slideIn, 0) - 1) + var(--SideNavigation-slideIn, 0) * var(--Sidebar-width, 0px)))',
            lg: 'translateX(-100%)',
          },
        }}
        onClick={() => closeSidebar()}
      />
      <Box sx={{ display: 'flex', gap: 1, alignItems: 'center' }}>
        <IconButton variant="soft" color="primary" size="sm">
          <BrightnessAutoRoundedIcon />
        </IconButton>
        <Typography level="title-lg">Acme Co.</Typography>
        <ColorSchemeToggle sx={{ ml: 'auto' }} />
      </Box>
      <Box sx={{ minHeight: 0, overflow: 'hidden auto', flexGrow: 1, display: 'flex', flexDirection: 'column', [`& .${listItemButtonClasses.root}`]: { gap: 1.5, }, }}>
       
        <CustomMenu menu={menuItems} currentPath={currentPath} />
        <List
          size="sm"
          sx={{
            mt: 'auto',
            flexGrow: 0,
            '--ListItem-radius': (theme) => theme.vars.radius.sm,
            '--List-gap': '8px',
            mb: 2,
          }}
        >
          
        </List>
        
      </Box>
      <Divider />
      <Box sx={{ display: 'flex', gap: 1, alignItems: 'center' }}>
        <Avatar variant="outlined" size="sm" src="https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?auto=format&fit=crop&w=286"/>
        <Box sx={{ minWidth: 0, flex: 1 }}>
          <Typography level="title-sm">Siriwat K.</Typography>
          <Typography level="body-xs">siriwatk@test.com</Typography>
        </Box>
        <IconButton size="sm" variant="plain" color="neutral">
          <LogoutRoundedIcon />
        </IconButton>
      </Box>
    </Sheet>
  );
}
export type {MenuProps}