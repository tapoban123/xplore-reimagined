import express from 'express';
import pool from '../db.js'
import bcrypt from 'bcryptjs';
import jwt from 'jsonwebtoken';


const router = express.Router();

// Sign up
router.post('/signup', async (req, res) => {
  const { name, email, password } = req.body;
  try {
    const userExists = await pool.query('SELECT * FROM users WHERE email = $1', [email]);
    if (userExists.rows.length > 0) {
      return res.status(400).json({ message: 'User already exists' });
    }

    const hashedPassword = await bcrypt.hash(password, 10);
    await pool.query(
      'INSERT INTO users (name, email, password) VALUES ($1, $2, $3)',
      [name, email, hashedPassword]
    );

    res.status(201).json({ message: 'User created' });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Login
router.post('/login', async (req, res) => {
  const { email, password } = req.body;
  try {
    const user = await pool.query('SELECT * FROM users WHERE email = $1', [email]);
    if (user.rows.length === 0) {
      return res.status(400).json({ message: 'Invalid email' });
    }

    const valid = await bcrypt.compare(password, user.rows[0].password);
    if (!valid) {
      return res.status(400).json({ message: 'Invalid password' });
    }

    const token = jwt.sign({ id: user.rows[0].id }, process.env.JWT_SECRET);
    res.json({ token, user: { id: user.rows[0].id, name: user.rows[0].name } });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

export default router;
