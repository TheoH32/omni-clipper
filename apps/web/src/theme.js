import { extendTheme } from '@chakra-ui/react';

const config = {
  initialColorMode: 'dark',
  useSystemColorMode: false,
};

const theme = extendTheme({
  config,
  colors: {
    brand: {
      900: '#1a202c',
      800: '#2d3748',
      700: '#4a5568',
      600: '#718096',
      500: '#a0aec0',
      400: '#cbd5e0',
      300: '#e2e8f0',
      200: '#edf2f7',
      100: '#f7fafc',
    },
    accent: {
      blue: '#3182ce',
      purple: '#805ad5',
    },
  },
  styles: {
    global: {
      'html, body': {
        backgroundColor: 'brand.800',
        color: 'brand.100',
      },
    },
  },
});

export default theme;
