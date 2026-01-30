import {
  Avatar,
  Box,
  Flex,
  Heading,
  Menu,
  MenuButton,
  MenuDivider,
  MenuItem,
  MenuList,
  Text,
} from '@chakra-ui/react';
import { useAuth } from './AuthContext';

export default function Layout({ children }) {
  const { isAuthenticated, user, logout } = useAuth();

  return (
    <Box>
      <Flex
        as="header"
        align="center"
        justify="space-between"
        wrap="wrap"
        p="1.5rem"
        bg="brand.900"
        color="white"
      >
        <Flex align="center" mr={5}>
          <Heading as="h1" size="lg" letterSpacing="-0.1rem">
            Omni Clipper
          </Heading>
        </Flex>

        {isAuthenticated && (
          <Menu>
            <MenuButton
              p={0}
              borderRadius="full"
              _hover={{}}
              _active={{}}
              _focus={{ boxShadow: 'none' }}
            >
              <Avatar
                size="sm"
                name={user?.name}
                src="https://bit.ly/dan-abramov" // remove src if you want initials only
                cursor="pointer"
              />
            </MenuButton>

            <MenuList color="black">
              <Box p={2}>
                <Text fontWeight="bold">{user?.name}</Text>
                <Text fontSize="sm">{user?.email}</Text>
              </Box>

              <MenuDivider />

              <MenuItem>Settings</MenuItem>
              <MenuItem>User Profile</MenuItem>

              <MenuDivider />

              <MenuItem onClick={logout}>Log Out</MenuItem>
            </MenuList>
          </Menu>
        )}
      </Flex>

      <Box as="main" p={8}>
        {children}
      </Box>

      <Box as="footer" py={4} textAlign="center" bg="brand.900" color="white" />
    </Box>
  );
}
