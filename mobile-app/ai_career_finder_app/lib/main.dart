import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Xplore',
      theme: ThemeData.light(useMaterial3: true),
      home: const Scaffold(),
    );
  }
}
