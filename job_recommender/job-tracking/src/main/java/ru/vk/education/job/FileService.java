package ru.vk.education.job;
import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class FileService {
    private final String filePath;

    public FileService(String filePath) {
        this.filePath = filePath;
    }

    public void saveCmd(String command) {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(filePath, true))) {
            writer.write(command);
            writer.newLine();
        } catch (IOException e) {
            System.err.println("Exception during saving to file: " + e.getMessage());
        }
    }

    public List<String> readCommands() {
        Path path = Paths.get(filePath);
        if (!Files.exists(path)) {
            return new ArrayList<>();
        }
        try {
            return Files.readAllLines(path);
        } catch (IOException e) {
            System.err.println("Exception during reading from file: " + e.getMessage());
            return new ArrayList<>();
        }
    }
}